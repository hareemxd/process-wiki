import { PRSchema, type PRRecord } from "@/lib/schema/pr";
import { getOctokit, getRepo } from "@/lib/github/client";
import { makeIssueBody, extractPRRecordFromIssueBody } from "@/lib/github/prRecordBlock";

function statusLabel(status: PRRecord["status"]) {
  switch (status) {
    case "Open": return "pr:open";
    case "InProgress": return "pr:in-progress";
    case "ApprovedECR": return "pr:approved-ecr";
    case "Closed": return "pr:closed";
  }
}

function simpleLabel(key: string, value: string) {
  return `${key}:${value}`.toLowerCase().replace(/\s+/g, "-");
}

export async function getNextPRId(): Promise<string> {
  const octokit = getOctokit();
  const { owner, repo } = getRepo();

  // Search open+closed issues with PR- prefix in title.
  const q = `repo:${owner}/${repo} is:issue PR- in:title`;
  const res = await octokit.search.issuesAndPullRequests({ q, per_page: 100 });

  let max = 0;
  for (const item of res.data.items) {
    const m = item.title.match(/^PR-(\d+)\b/);
    if (m) max = Math.max(max, Number(m[1]));
  }
  return `PR-${max + 1}`;
}

export async function createPR(prInput: Omit<PRRecord, "prId" | "schemaVersion">): Promise<{ issueNumber: number; url: string; pr: PRRecord; }> {
  const octokit = getOctokit();
  const { owner, repo } = getRepo();

  const prId = await getNextPRId();

  const pr: PRRecord = PRSchema.parse({
    schemaVersion: "pr-0.1",
    prId,
    ...prInput,
  });

  const title = `${pr.prId}: ${pr.summary.slice(0, 80).replace(/\s+/g, " ").trim()}`;
  const body = makeIssueBody(pr);

  const labels = [
    statusLabel(pr.status),
    simpleLabel("source", pr.source),
    simpleLabel("reason", pr.reasonCategory === "CorrectiveAction" ? "corrective-action" : "improvement"),
    simpleLabel("type", pr.itemType),
  ];

  const created = await octokit.issues.create({
    owner,
    repo,
    title,
    body,
    labels,
  });

  return { issueNumber: created.data.number, url: created.data.html_url, pr };
}

export async function getPR(issueNumber: number): Promise<{ issueNumber: number; url: string; pr: PRRecord; title: string; }> {
  const octokit = getOctokit();
  const { owner, repo } = getRepo();

  const issue = await octokit.issues.get({ owner, repo, issue_number: issueNumber });
  const body = issue.data.body ?? "";

  const raw = extractPRRecordFromIssueBody(body);
  const pr = PRSchema.parse(raw);

  return { issueNumber, url: issue.data.html_url, pr, title: issue.data.title };
}

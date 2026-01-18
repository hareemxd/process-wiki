import { Octokit } from "@octokit/rest";

export function getOctokit() {
  const token = process.env.GITHUB_TOKEN;
  if (!token) throw new Error("Missing GITHUB_TOKEN in .env.local");
  return new Octokit({ auth: token });
}

export function getRepo() {
  const owner = process.env.GITHUB_OWNER;
  const repo = process.env.GITHUB_REPO;
  if (!owner || !repo) throw new Error("Missing GITHUB_OWNER or GITHUB_REPO in .env.local");
  return { owner, repo };
}

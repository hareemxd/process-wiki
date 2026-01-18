import type { PRRecord } from "@/lib/schema/pr";

const BEGIN = "<!-- pr-record:begin -->";
const END = "<!-- pr-record:end -->";

export function makeIssueBody(pr: PRRecord): string {
  const json = JSON.stringify(pr, null, 2);

  return `# Problem Report

${BEGIN}
\`\`\`json
${json}
\`\`\`
${END}

## Summary
- **Status:** ${pr.status}
- **Date received:** ${pr.dateReceived}
- **Submitted by:** ${pr.submittedBy.name}${pr.submittedBy.organization ? ` (${pr.submittedBy.organization})` : ""}
- **Source:** ${pr.source}
- **Reason category:** ${pr.reasonCategory}
- **Initiating part number:** ${pr.initiatingPartNumber}
- **Item type:** ${pr.itemType}
- **Current revision:** ${pr.currentRevision}
- **Owner:** ${pr.owner}

## Problem summary
${pr.summary}
`;
}

export function extractPRRecordFromIssueBody(body: string): unknown {
  const beginIdx = body.indexOf(BEGIN);
  const endIdx = body.indexOf(END);
  if (beginIdx === -1 || endIdx === -1 || endIdx <= beginIdx) {
    throw new Error("PR record block not found in issue body.");
  }

  const block = body.slice(beginIdx, endIdx);
  const fenceStart = block.indexOf("```json");
  if (fenceStart === -1) throw new Error("JSON fence not found in PR record block.");

  const afterFence = block.slice(fenceStart + "```json".length);
  const fenceEnd = afterFence.indexOf("```");
  if (fenceEnd === -1) throw new Error("Closing JSON fence not found.");

  const jsonText = afterFence.slice(0, fenceEnd).trim();
  return JSON.parse(jsonText);
}

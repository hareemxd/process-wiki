import Link from "next/link";

async function getData(number: string) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_BASE_URL ?? ""}/api/pr/${number}`, { cache: "no-store" });
  return res.json();
}

export default async function PRPage({ params }: { params: { number: string } }) {
  const data = await getData(params.number);

  if (data?.error) {
    return (
      <main className="mx-auto max-w-2xl p-6">
        <h1 className="text-2xl font-semibold">PR Viewer</h1>
        <p className="mt-4 rounded-lg border p-3 text-sm">{data.error}</p>
        <div className="mt-4">
          <Link className="underline" href="/new">Create a PR</Link>
        </div>
      </main>
    );
  }

  const { pr, issueNumber, url, title } = data;

  return (
    <main className="mx-auto max-w-2xl p-6">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h1 className="text-2xl font-semibold">{pr.prId}</h1>
          <p className="mt-1 text-sm opacity-70">{title}</p>
        </div>
        <a className="underline" href={url} target="_blank" rel="noreferrer">
          Open in GitHub
        </a>
      </div>

      <div className="mt-6 rounded-lg border p-4 text-sm">
        <div className="grid grid-cols-1 gap-2">
          <div><b>Status:</b> {pr.status}</div>
          <div><b>Date received:</b> {pr.dateReceived}</div>
          <div><b>Submitted by:</b> {pr.submittedBy.name}{pr.submittedBy.organization ? ` (${pr.submittedBy.organization})` : ""}</div>
          <div><b>Source:</b> {pr.source}</div>
          <div><b>Reason category:</b> {pr.reasonCategory}</div>
          <div><b>Initiating PN:</b> {pr.initiatingPartNumber}</div>
          <div><b>Item type:</b> {pr.itemType}</div>
          <div><b>Current revision:</b> {pr.currentRevision}</div>
          <div><b>Owner:</b> {pr.owner}</div>
        </div>
      </div>

      <div className="mt-6">
        <h2 className="text-lg font-semibold">Problem summary</h2>
        <p className="mt-2 whitespace-pre-wrap">{pr.summary}</p>
      </div>

      <div className="mt-8">
        <Link className="underline" href="/new">Create another PR</Link>
      </div>
    </main>
  );
}

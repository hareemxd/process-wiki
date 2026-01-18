"use client";

import { useMemo, useState } from "react";
import { PRSchema, PR_SOURCE, PR_REASON_CATEGORY, PR_ITEM_TYPE, PR_STATUS } from "@/lib/schema/pr";

type Draft = {
  status: (typeof PR_STATUS)[number];
  dateReceived: string;
  submittedBy: { name: string; organization?: string };
  source: (typeof PR_SOURCE)[number];
  reasonCategory: (typeof PR_REASON_CATEGORY)[number];
  summary: string;
  initiatingPartNumber: string;
  itemType: (typeof PR_ITEM_TYPE)[number];
  currentRevision: string;
  owner: string;
};

function todayISO() {
  const d = new Date();
  const yyyy = d.getFullYear();
  const mm = String(d.getMonth() + 1).padStart(2, "0");
  const dd = String(d.getDate()).padStart(2, "0");
  return `${yyyy}-${mm}-${dd}`;
}

export default function NewPRPage() {
  const [step, setStep] = useState(1);
  const [saving, setSaving] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [created, setCreated] = useState<{ issueNumber: number; url: string } | null>(null);

  const [draft, setDraft] = useState<Draft>({
    status: "Open",
    dateReceived: todayISO(),
    submittedBy: { name: "", organization: "" },
    source: "Internal",
    reasonCategory: "CorrectiveAction",
    summary: "",
    initiatingPartNumber: "",
    itemType: "Documentation",
    currentRevision: "",
    owner: "",
  });

  const canNext = useMemo(() => {
    if (step === 1) {
      return draft.submittedBy.name.trim().length > 0 && draft.summary.trim().length > 0;
    }
    if (step === 2) {
      return draft.initiatingPartNumber.trim().length > 0 && draft.currentRevision.trim().length > 0;
    }
    if (step === 3) {
      return draft.owner.trim().length > 0;
    }
    return false;
  }, [step, draft]);

  async function submit() {
    setErr(null);
    setSaving(true);
    try {
      // Validate via Zod schema (client-side) – synthesize prId on server
      PRSchema.omit({ prId: true, schemaVersion: true }).parse(draft);

      const res = await fetch("/api/pr/create", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(draft),
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data?.error ?? "Failed to create PR.");

      setCreated({ issueNumber: data.issueNumber, url: data.url });
    } catch (e: any) {
      setErr(e?.message ?? "Unknown error");
    } finally {
      setSaving(false);
    }
  }

  if (created) {
    return (
      <main className="mx-auto max-w-2xl p-6">
        <h1 className="text-2xl font-semibold">Created</h1>
        <p className="mt-2">
          PR created as GitHub Issue #{created.issueNumber}.
        </p>
        <div className="mt-4 flex gap-3">
          <a className="underline" href={created.url} target="_blank" rel="noreferrer">Open in GitHub</a>
          <a className="underline" href={`/pr/${created.issueNumber}`}>View in app</a>
        </div>
      </main>
    );
  }

  return (
    <main className="mx-auto max-w-2xl p-6">
      <h1 className="text-2xl font-semibold">New Problem Report</h1>
      <p className="mt-1 text-sm opacity-70">Step {step} of 3</p>

      {err && (
        <div className="mt-4 rounded-lg border p-3 text-sm">
          <div className="font-semibold">Error</div>
          <div className="mt-1">{err}</div>
        </div>
      )}

      {/* Step 1: Intake */}
      {step === 1 && (
        <section className="mt-6 space-y-4">
          <div className="grid gap-2">
            <label className="text-sm font-medium">Date received</label>
            <input
              className="rounded-lg border p-2"
              value={draft.dateReceived}
              onChange={(e) => setDraft({ ...draft, dateReceived: e.target.value })}
              placeholder="YYYY-MM-DD"
            />
          </div>

          <div className="grid gap-2">
            <label className="text-sm font-medium">Submitted by (name)</label>
            <input
              className="rounded-lg border p-2"
              value={draft.submittedBy.name}
              onChange={(e) => setDraft({ ...draft, submittedBy: { ...draft.submittedBy, name: e.target.value } })}
            />
          </div>

          <div className="grid gap-2">
            <label className="text-sm font-medium">Submitted by (organization)</label>
            <input
              className="rounded-lg border p-2"
              value={draft.submittedBy.organization ?? ""}
              onChange={(e) => setDraft({ ...draft, submittedBy: { ...draft.submittedBy, organization: e.target.value } })}
            />
          </div>

          <div className="grid gap-2">
            <label className="text-sm font-medium">Source</label>
            <select
              className="rounded-lg border p-2"
              value={draft.source}
              onChange={(e) => setDraft({ ...draft, source: e.target.value as Draft["source"] })}
            >
              <option value="Internal">Internal</option>
              <option value="External">External</option>
            </select>
          </div>

          <div className="grid gap-2">
            <label className="text-sm font-medium">Reason category</label>
            <select
              className="rounded-lg border p-2"
              value={draft.reasonCategory}
              onChange={(e) => setDraft({ ...draft, reasonCategory: e.target.value as Draft["reasonCategory"] })}
            >
              <option value="CorrectiveAction">Corrective Action</option>
              <option value="Improvement">Improvement</option>
            </select>
          </div>

          <div className="grid gap-2">
            <label className="text-sm font-medium">Summary</label>
            <textarea
              className="min-h-[140px] rounded-lg border p-2"
              value={draft.summary}
              onChange={(e) => setDraft({ ...draft, summary: e.target.value })}
              placeholder="Describe the problem."
            />
          </div>
        </section>
      )}

      {/* Step 2: Item Identification */}
      {step === 2 && (
        <section className="mt-6 space-y-4">
          <div className="grid gap-2">
            <label className="text-sm font-medium">Initiating part number</label>
            <input
              className="rounded-lg border p-2"
              value={draft.initiatingPartNumber}
              onChange={(e) => setDraft({ ...draft, initiatingPartNumber: e.target.value })}
            />
          </div>

          <div className="grid gap-2">
            <label className="text-sm font-medium">Item type</label>
            <select
              className="rounded-lg border p-2"
              value={draft.itemType}
              onChange={(e) => setDraft({ ...draft, itemType: e.target.value as Draft["itemType"] })}
            >
              <option value="Hardware">Hardware</option>
              <option value="Software">Software</option>
              <option value="Documentation">Documentation</option>
            </select>
          </div>

          <div className="grid gap-2">
            <label className="text-sm font-medium">Current revision</label>
            <input
              className="rounded-lg border p-2"
              value={draft.currentRevision}
              onChange={(e) => setDraft({ ...draft, currentRevision: e.target.value })}
              placeholder="A, A.1, 1.0, etc."
            />
          </div>
        </section>
      )}

      {/* Step 3: Ownership & Review */}
      {step === 3 && (
        <section className="mt-6 space-y-4">
          <div className="grid gap-2">
            <label className="text-sm font-medium">Owner (CM assigned)</label>
            <input
              className="rounded-lg border p-2"
              value={draft.owner}
              onChange={(e) => setDraft({ ...draft, owner: e.target.value })}
            />
          </div>

          <div className="grid gap-2">
            <label className="text-sm font-medium">Status (default)</label>
            <select
              className="rounded-lg border p-2"
              value={draft.status}
              onChange={(e) => setDraft({ ...draft, status: e.target.value as Draft["status"] })}
            >
              <option value="Open">Open</option>
              <option value="InProgress">In Progress</option>
              <option value="ApprovedECR">Approved – ECR</option>
              <option value="Closed">Closed</option>
            </select>
          </div>

          <div className="rounded-lg border p-3 text-sm">
            <div className="font-semibold">Preview (high level)</div>
            <ul className="mt-2 space-y-1">
              <li><b>Date:</b> {draft.dateReceived}</li>
              <li><b>Submitted by:</b> {draft.submittedBy.name}{draft.submittedBy.organization ? ` (${draft.submittedBy.organization})` : ""}</li>
              <li><b>Source:</b> {draft.source}</li>
              <li><b>Reason:</b> {draft.reasonCategory}</li>
              <li><b>PN:</b> {draft.initiatingPartNumber}</li>
              <li><b>Type:</b> {draft.itemType}</li>
              <li><b>Rev:</b> {draft.currentRevision}</li>
              <li><b>Owner:</b> {draft.owner}</li>
            </ul>
          </div>
        </section>
      )}

      <div className="mt-8 flex items-center justify-between">
        <button
          className="rounded-lg border px-4 py-2 disabled:opacity-50"
          disabled={step === 1 || saving}
          onClick={() => setStep((s) => Math.max(1, s - 1))}
        >
          Back
        </button>

        {step < 3 ? (
          <button
            className="rounded-lg border px-4 py-2 disabled:opacity-50"
            disabled={!canNext || saving}
            onClick={() => setStep((s) => Math.min(3, s + 1))}
          >
            Next
          </button>
        ) : (
          <button
            className="rounded-lg border px-4 py-2 disabled:opacity-50"
            disabled={!canNext || saving}
            onClick={submit}
          >
            {saving ? "Creating…" : "Create PR"}
          </button>
        )}
      </div>
    </main>
  );
}

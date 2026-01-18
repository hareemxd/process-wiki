import { NextResponse } from "next/server";
import { createPR } from "@/lib/github/prStore";
import { z } from "zod";

const CreatePayload = z.object({
  status: z.enum(["Open", "InProgress", "ApprovedECR", "Closed"]).default("Open"),
  dateReceived: z.string(),
  submittedBy: z.object({
    name: z.string(),
    organization: z.string().optional().default(""),
  }),
  source: z.enum(["Internal", "External"]),
  reasonCategory: z.enum(["CorrectiveAction", "Improvement"]),
  summary: z.string(),
  initiatingPartNumber: z.string(),
  itemType: z.enum(["Hardware", "Software", "Documentation"]),
  currentRevision: z.string(),
  owner: z.string(),
});

export async function POST(req: Request) {
  try {
    const json = await req.json();
    const payload = CreatePayload.parse(json);

    const created = await createPR(payload);
    return NextResponse.json(created, { status: 200 });
  } catch (err: any) {
    return NextResponse.json(
      { error: err?.message ?? "Unknown error" },
      { status: 400 }
    );
  }
}

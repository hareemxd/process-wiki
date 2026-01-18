import { NextResponse } from "next/server";
import { getPR } from "@/lib/github/prStore";

export async function GET(_req: Request, context: { params: { number: string } }) {
  try {
    const issueNumber = Number(context.params.number);
    if (!Number.isFinite(issueNumber)) throw new Error("Invalid issue number.");

    const data = await getPR(issueNumber);
    return NextResponse.json(data, { status: 200 });
  } catch (err: any) {
    return NextResponse.json(
      { error: err?.message ?? "Unknown error" },
      { status: 400 }
    );
  }
}

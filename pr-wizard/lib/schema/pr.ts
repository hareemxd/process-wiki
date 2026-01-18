import { z } from "zod";

export const PR_STATUS = ["Open", "InProgress", "ApprovedECR", "Closed"] as const;
export const PR_SOURCE = ["Internal", "External"] as const;
export const PR_REASON_CATEGORY = ["CorrectiveAction", "Improvement"] as const;
export const PR_ITEM_TYPE = ["Hardware", "Software", "Documentation"] as const;

export const PRSchema = z.object({
  schemaVersion: z.literal("pr-0.1"),

  prId: z
    .string()
    .min(1)
    .regex(/^PR-\d+$/, "prId must look like PR-1, PR-2, etc."),

  status: z.enum(PR_STATUS).default("Open"),

  dateReceived: z
    .string()
    .regex(/^\d{4}-\d{2}-\d{2}$/, "dateReceived must be YYYY-MM-DD"),

  submittedBy: z.object({
    name: z.string().min(1, "submittedBy.name is required"),
    organization: z.string().optional().default(""),
  }),

  source: z.enum(PR_SOURCE),
  reasonCategory: z.enum(PR_REASON_CATEGORY),

  summary: z.string().min(1, "summary is required"),

  initiatingPartNumber: z.string().min(1, "initiatingPartNumber is required"),
  itemType: z.enum(PR_ITEM_TYPE),

  currentRevision: z.string().min(1, "currentRevision is required"),

  owner: z.string().min(1, "owner is required"),
});

export type PRRecord = z.infer<typeof PRSchema>;

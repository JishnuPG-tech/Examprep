# Pipeline contract

## Input
PDF document plus exam identifier, optional year/cycle, optional section and source metadata.

## Output states
validated: structural checks pass, answer exists, confidence threshold passes and provenance exists.
rejected: malformed or incomplete record.
review: useful candidate but confidence or evidence is insufficient.

## Non-negotiable invariants
1. Every question has a source document.
2. Every question has a content hash.
3. Every MCQ has unique option labels.
4. An answer key must reference an existing option.
5. Missing answers are never guessed.
6. Duplicate source documents are idempotent.
7. Model output is schema-validated before use.
8. Low-confidence records do not enter the validated set.

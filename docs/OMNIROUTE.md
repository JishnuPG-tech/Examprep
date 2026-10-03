# OmniRoute integration

Examprep treats OmniRoute as an optional model gateway, not as part of the
deterministic extraction core.

OmniRoute exposes an OpenAI-compatible API and can route requests across
multiple model/provider connections. This is useful for difficult processing
tasks such as question-boundary reconstruction, semantic classification,
diagram/table interpretation, answer reconciliation, and explanation generation.

## Configuration

    OMNIROUTE_ENABLED=true
    OMNIROUTE_BASE_URL=http://localhost:20128/v1
    OMNIROUTE_API_KEY=<gateway-key-if-required>
    OMNIROUTE_MODEL=<model-id>

Optional:

    OMNIROUTE_ROUTE_MODEL=<provider/model override>
    OMNIROUTE_MODE=<gateway mode>
    OMNIROUTE_BUDGET_USD=<per-request hard budget>
    OMNIROUTE_TIMEOUT_SECONDS=120

The exact model IDs and routing modes belong to the deployed OmniRoute
instance and are deliberately not hard-coded into Examprep.

## Architecture

    PDF
      |
      +--> deterministic extraction -------------------+
      |                                                 |
      +--> OCR/layout/math/table/diagram extraction ---+--> canonical elements
                                                        |
                                                        +--> model enrichment
                                                               |
                                                               v
                                                            OmniRoute
                                                               |
                                             +-----------------+----------------+
                                             |                 |                |
                                          model A           model B          model C
                                             |                 |                |
                                             +-----------------+----------------+
                                                               |
                                                               v
                                                        validated structure

The deterministic and visual evidence remains authoritative. A model may
interpret or classify extracted evidence, but it must not silently replace
the source representation.

## Recommended routing classes

- layout_understanding: multimodal/vision-capable model
- math_parsing: strong mathematical/reasoning model
- question_classification: fast structured-output model
- answer_verification: independent reasoning model
- diagram_interpretation: vision-capable reasoning model
- table_reconstruction: vision/table-capable model
- current_affairs_normalization: fast extraction model

For high-risk fields, use two independent model passes when budget allows and
send disagreements to human review. Never treat model consensus alone as proof.

## Provenance

Every model-assisted result should eventually record:

- provider: omniroute
- model
- route model, when used
- request/task type
- extractor version
- timestamp
- source evidence references
- confidence
- validation state

## Failure behaviour

If OmniRoute is unavailable or times out, Examprep must not invent data.
The current pipeline records model_failed and leaves deterministic results
untouched. Later stages can quarantine the document for retry/review.

## Security

Never commit OmniRoute credentials. Use environment variables or a secret
manager. If the gateway is remote, use HTTPS and a scoped gateway token.

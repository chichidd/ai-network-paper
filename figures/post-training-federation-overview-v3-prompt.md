# SiloStitch overview figure — final generation prompt

Mode: built-in GPT Image generation, edited from
`post-training-federation-hypervision-style-v2.png`.

Create a clean, publication-ready, very wide academic workflow figure on a
white background. Use crisp vector-like line art, thin charcoal outlines,
restrained navy accents, green only for candidate adoption, and amber only for
retaining the audited incumbent. Avoid gradients, shadows, 3-D objects, locks,
shields, decorative icons, formulas, legends, captions, and watermarks.

Organize the figure into three left-to-right stages:

1. **Package Registration.** Treat “Historical training data unavailable” as
   a small gray context note, not a pipeline input. Show frozen detector
   packages entering a registry that checks version, integrity, and interface,
   then distributes one versioned package pool with a common score interface
   to all sites.

2. **Collaborative Candidate Construction.** Expand only one representative
   site. Keep its local fit set and incumbent-plus-auxiliary scores within the
   site boundary. Show the residual composer producing an encoded gradient;
   gradients from all sites enter secure aggregation. The coordinator receives
   the decoded aggregate gradient, forms shared composer $W_G$, and returns it
   to the sites. Never use “Accepted Aggregate” and do not imply differential
   privacy or resistance to inference. State that per-example site data remain
   local.

   Draw an explicit cross-stage handoff from the registered package pool into
   candidate construction. Draw a second explicit handoff from the
   coordinator's $W_G$ to the site-local $W_G$ used by personalization.

3. **Site-Local Deployment Authorization.** Show shared composer $W_G$ and the
   local fit set entering personalization to produce candidate $W_j$. Freeze
   the candidate and audit rule before opening the held-out audit set. A paired
   audit compares the frozen candidate with the audited incumbent and ends in
   exactly two valid-audit outcomes: “Adopt Candidate” or “Use Audited
   Incumbent.” Both outcomes must leave one shared decision diamond labeled
   “All Bounds Within Tolerance?”; the predictor boxes must not connect
   independently to the outcomes. Do not show runtime failure handling in this
   overview.

Keep all labels horizontal and readable at two-column paper width. Preserve
arrow direction: package pool to sites, site gradients to secure aggregation,
aggregate to coordinator, shared composer from coordinator back to sites, and
the local authorization sequence from personalization through the paired
audit.

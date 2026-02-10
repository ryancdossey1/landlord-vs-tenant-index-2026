# 2026 Landlord vs. Tenant State Rankings — All 50 US States

**Version:** v2026.1 | **Last updated:** February 2026

Scored index ranking all 50 US states on how landlord-friendly or tenant-friendly their laws are, across 10 weighted legal and financial factors on a 1–5 scale.

This dataset is part of the [SoldFast Housing Policy Research](https://soldfast.com/blog/) series.

## Download & Explore

| Platform | Link |
|----------|------|
| 📊 **Full Analysis** | [soldfast.com/blog/is-your-state-more-tenant-friendly-or-landlord-friendly/](https://soldfast.com/blog/is-your-state-more-tenant-friendly-or-landlord-friendly/) |
| 🗺️ **Interactive Map** | [ryancdossey1.github.io/landlord-vs-tenant-index-2026/interactive-map.html](https://ryancdossey1.github.io/landlord-vs-tenant-index-2026/interactive-map.html) |
| 🤗 **Hugging Face** | [huggingface.co/datasets/ryancdossey1/2026-landlord-vs-tenant-state-rankings-index](https://huggingface.co/datasets/ryancdossey1/2026-landlord-vs-tenant-state-rankings-index) |
| 📈 **Kaggle** | [DOI: 10.34740/KAGGLE/DSV/14757559](https://doi.org/10.34740/KAGGLE/DSV/14757559) |
| 🏛️ **Zenodo** | [DOI: 10.5281/zenodo.18512494](https://doi.org/10.5281/zenodo.18512494) |

## Factors Scored

Each state is evaluated on 10 factors (1 = most tenant-friendly, 5 = most landlord-friendly), grouped into weighted categories:

| Category | Weight | Factors |
|----------|--------|---------|
| **Legal** | 35% | Formal Landlord/Tenant Act, Rent Control, Regulatory Burdens |
| **Evictions** | 35% | Eviction Timelines, Notice Periods, Eviction Costs |
| **Financial** | 20% | Security Deposits, Late Fees, Property Tax Rates |
| **Miscellaneous** | 10% | Adverse Possession |

**Formula:** `(Legal Avg × 0.35) + (Eviction Avg × 0.35) + (Financial Avg × 0.20) + (Misc Avg × 0.10)`

## Source & Methodology

- Full analysis: https://soldfast.com/blog/is-your-state-more-tenant-friendly-or-landlord-friendly/
- Methodology: https://soldfast.com/blog/our-methodology-for-the-2026-landlord-vs-tenant-state-rankings/
- Published by SoldFast | Author: Connor White
- Updated quarterly

## Citation

```bibtex
@dataset{soldfast_landlord_tenant_2026,
  title     = {SoldFast Landlord vs. Tenant State Rankings Index 2026},
  author    = {White, Connor},
  year      = {2026},
  publisher = {SoldFast},
  url       = {https://soldfast.com/blog/is-your-state-more-tenant-friendly-or-landlord-friendly/},
  doi       = {10.5281/zenodo.18512494},
  license   = {CC-BY-4.0}
}
```

## License

CC BY 4.0 — free to use with attribution.

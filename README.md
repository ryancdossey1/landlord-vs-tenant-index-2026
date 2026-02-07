# 2026 Landlord vs. Tenant State Rankings Index

A composite scoring of all 50 U.S. states across 10 legal and financial factors, ranking each on a 1–5 scale from tenant-friendly to landlord-friendly. Built by [SoldFast](https://soldfast.com).

## Interactive Map

**[View the Interactive Map →](https://ryancdossey1.github.io/landlord-vs-tenant-index-2026/interactive-map.html)**

A mobile-responsive, all-blue choropleth map with hover tooltips (desktop), tap-to-preview modals (mobile), a state dropdown selector, and a searchable/sortable data table covering all 50 states and every factor score. Every state links directly to its section in the full blog analysis.

## About the Index

Each state is scored across 10 factors that shape the landlord-tenant relationship:

| Factor | What It Measures |
|---|---|
| Formal Landlord-Tenant Act | Whether the state has a comprehensive statutory framework |
| Rent Control Programs | Presence and restrictiveness of rent control or stabilization |
| Regulatory Burdens | Licensing, registration, and compliance requirements for landlords |
| Potential Eviction Costs | Legal fees, court costs, and financial exposure during evictions |
| Avg Eviction Timelines | How long the eviction process takes from notice to possession |
| Required Notice Periods | Mandatory notice windows for rent increases, entry, and termination |
| Effective Property Tax Rate | State-level property tax burden as a percentage of value |
| Adverse Possession Requirements | How difficult it is for squatters to claim property rights |
| Security Deposit Rules | Caps, return timelines, and itemization requirements |
| Late Fee Rules | Restrictions on late rent penalties and grace periods |

Scores are averaged into a composite **Overall Score** (1.0 = strongly tenant-friendly, 5.0 = strongly landlord-friendly).

## Key Findings

- **Most landlord-friendly:** North Dakota (4.6), Wyoming (4.5), Utah (4.4)
- **Most tenant-friendly:** New Jersey (1.8), California (1.9), Washington (1.9)
- **National median:** 3.85

## Read the Full Analysis

- **[State-by-State Breakdown](https://soldfast.com/blog/is-your-state-more-tenant-friendly-or-landlord-friendly/)** — detailed analysis of all 50 states with policy context
- **[Methodology](https://soldfast.com/blog/our-methodology-for-the-2026-landlord-vs-tenant-state-rankings/)** — scoring criteria, data sources, and research process

## Dataset & Citation

The complete dataset is published as open data on two platforms:

| Platform | DOI | Link |
|---|---|---|
| **Zenodo** | `10.5281/zenodo.18512494` | [doi.org/10.5281/zenodo.18512494](https://doi.org/10.5281/zenodo.18512494) |
| **Kaggle** | `10.34740/KAGGLE/DSV/14757559` | [doi.org/10.34740/kaggle/dsv/14757559](https://doi.org/10.34740/kaggle/dsv/14757559) |

Available in CSV, JSON, and XLSX formats. Licensed for reuse with attribution.

### APA Citation

> White, C. (2026). *2026 Landlord vs. Tenant State Rankings Index* [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.18512494

### BibTeX

```bibtex
@misc{connor_white_2026,
    title={2026 Landlord vs. Tenant State Rankings Index},
    author={Connor White},
    year={2026},
    doi={10.5281/zenodo.18512494},
    publisher={Zenodo},
    url={https://doi.org/10.5281/zenodo.18512494}
}
```

## Repository Contents

| File | Description |
|---|---|
| `interactive-map.html` | Full interactive map with data table, search, and sort |
| `exploratory_analysis.py` | Python exploratory analysis script |
| `Landlord Vs. Tenant Index.csv` | Raw dataset in CSV format |
| `README.md` | This file |

## Tech

Single-file HTML/CSS/JavaScript. No build step required.

- [D3.js](https://d3js.org/) for map rendering
- [TopoJSON](https://github.com/topojson/topojson) for U.S. state geometries
- [DM Sans](https://fonts.google.com/specimen/DM+Sans) via Google Fonts
- GitHub Pages for hosting

## License

Dataset: Open data, free to reuse with attribution.

Interactive map and analysis: © 2026 [SoldFast](https://soldfast.com). All rights reserved.

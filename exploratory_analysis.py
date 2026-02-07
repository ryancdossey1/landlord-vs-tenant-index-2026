import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import Patch

# Load the dataset
df = pd.read_csv("Landlord Vs. Tenant Index.csv")

# Quick look at the data
print(f"Dataset: {df.shape[0]} states × {df.shape[1]} columns\n")
print(df.head(10))

# --- Overall Score Distribution ---
print("\n--- Summary Statistics ---")
print(df['Overall_Score'].describe())

# --- Verdict Breakdown ---
print("\n--- Verdict Counts ---")
print(df['Verdict'].value_counts())

# --- Top 5 Most Landlord-Friendly States ---
top_landlord = df.nlargest(5, 'Overall_Score')[['State', 'Overall_Score', 'Verdict']]
print("\n--- Top 5 Most Landlord-Friendly States ---")
print(top_landlord.to_string(index=False))

# --- Top 5 Most Tenant-Friendly States ---
top_tenant = df.nsmallest(5, 'Overall_Score')[['State', 'Overall_Score', 'Verdict']]
print("\n--- Top 5 Most Tenant-Friendly States ---")
print(top_tenant.to_string(index=False))

# --- Bar Chart: All 50 States Ranked by Overall Score ---
fig, ax = plt.subplots(figsize=(12, 14))

df_sorted = df.sort_values('Overall_Score', ascending=True)

colors = []
for v in df_sorted['Verdict']:
    v_lower = v.strip().lower()
    if 'landlord' in v_lower:
        colors.append('#c0392b')
    elif 'tenant' in v_lower:
        colors.append('#2980b9')
    else:
        colors.append('#7f8c8d')

ax.barh(df_sorted['State'], df_sorted['Overall_Score'], color=colors)
ax.set_xlabel('Overall Score (1 = Tenant-Friendly → 5 = Landlord-Friendly)', fontsize=11)
ax.set_title('2026 Landlord vs. Tenant State Rankings — All 50 States', fontsize=14, fontweight='bold')
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.set_xlim(1, 5)

legend_elements = [
    Patch(facecolor='#c0392b', label='Landlord-Friendly'),
    Patch(facecolor='#7f8c8d', label='Neutral'),
    Patch(facecolor='#2980b9', label='Tenant-Friendly')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

plt.tight_layout()
plt.savefig('state_rankings_bar_chart.png', dpi=150)
plt.show()

# --- Heatmap: Factor Scores by State ---
factor_cols = [
    'Formal_Landlord_Tenant_Act', 'Rent_Control_Programs', 'Regulatory_Burdens',
    'Potential_Eviction_Costs', 'Avg_Eviction_Rates_Timelines', 'Required_Notice_Periods',
    'Effective_Property_Tax_Rate', 'Adverse_Possession_Requirements',
    'Security_Deposit_Rules', 'Late_Fee_Rules'
]

fig, ax = plt.subplots(figsize=(14, 16))

df_heat = df.sort_values('Overall_Score', ascending=False).set_index('State')[factor_cols]

im = ax.imshow(df_heat.values, cmap='RdYlBu_r', aspect='auto', vmin=1, vmax=5)

ax.set_xticks(range(len(factor_cols)))
ax.set_xticklabels([c.replace('_', ' ') for c in factor_cols], rotation=45, ha='right', fontsize=9)
ax.set_yticks(range(len(df_heat)))
ax.set_yticklabels(df_heat.index, fontsize=8)
ax.set_title('Factor Scores by State (Sorted by Overall Score)', fontsize=14, fontweight='bold')

cbar = plt.colorbar(im, ax=ax, shrink=0.5)
cbar.set_label('Score (1 = Tenant-Friendly → 5 = Landlord-Friendly)', fontsize=10)

plt.tight_layout()
plt.savefig('factor_heatmap.png', dpi=150)
plt.show()

# --- Correlation Matrix ---
fig, ax = plt.subplots(figsize=(10, 8))

corr = df[factor_cols + ['Overall_Score']].corr()

im = ax.imshow(corr.values, cmap='coolwarm', vmin=-1, vmax=1)

labels = [c.replace('_', ' ') for c in corr.columns]
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, fontsize=9)
ax.set_title('Factor Correlation Matrix', fontsize=14, fontweight='bold')

for i in range(len(corr)):
    for j in range(len(corr)):
        ax.text(j, i, f'{corr.values[i, j]:.2f}', ha='center', va='center', fontsize=7,
                color='white' if abs(corr.values[i, j]) > 0.5 else 'black')

plt.colorbar(im, ax=ax, shrink=0.8)
plt.tight_layout()
plt.savefig('correlation_matrix.png', dpi=150)
plt.show()

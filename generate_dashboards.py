"""Automated Sustainability Dashboard Generator

Task: Week 4 - Sustainability Metrics Reporting and Visualization Strategy
Internship: Virtual Sustainability SQL Development Intern
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set global visual style
sns.set_theme(style='whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'


def generate_sample_data() -> tuple[pd.DataFrame, pd.DataFrame]:
  """Generates sample sustainability data reflecting SQL view outputs."""
  # Monthly Energy & Carbon Data
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
  energy_data = {
      'month': months,
      'energy_kwh': [125000, 132000, 118000, 140000, 135000, 128000],
      'carbon_tonnes': [88.5, 92.1, 81.4, 98.2, 94.0, 89.6],
  }
  df_monthly = pd.DataFrame(energy_data)

  # Facility Waste Diversion Data
  facility_data = {
      'facility_name': [
          'Berlin Tech',
          'Dallas Sorting',
          'Munich Hub',
          'Chicago Center',
      ],
      'diversion_rate': [85.0, 78.5, 70.0, 82.3],
      'target': [80.0, 80.0, 80.0, 80.0],
  }
  df_facility = pd.DataFrame(facility_data)

  return df_monthly, df_facility


def plot_energy_carbon_trend(df_monthly: pd.DataFrame):
  """Plots dual-axis Monthly Energy Consumption vs Carbon Footprint."""
  fig, ax1 = plt.subplots(figsize=(10, 5))

  color = '#1f77b4'
  ax1.set_xlabel('Reporting Month (2026)', fontweight='bold')
  ax1.set_ylabel('Total Energy (kWh)', color=color, fontweight='bold')
  bars = ax1.bar(
      df_monthly['month'],
      df_monthly['energy_kwh'],
      color=color,
      alpha=0.7,
      width=0.4,
      label='Energy (kWh)',
  )
  ax1.tick_params(axis='y', labelcolor=color)

  # Secondary axis for Carbon
  ax2 = ax1.twinx()
  color = '#2ca02c'
  ax2.set_ylabel('Carbon Emissions (tCO2e)', color=color, fontweight='bold')
  line = ax2.plot(
      df_monthly['month'],
      df_monthly['carbon_tonnes'],
      color=color,
      marker='o',
      linewidth=2.5,
      label='Carbon Footprint',
  )
  ax2.tick_params(axis='y', labelcolor=color)

  plt.title(
      'Monthly Energy Consumption vs Carbon Emissions',
      fontsize=14,
      fontweight='bold',
      pad=15,
  )
  fig.tight_layout()
  plt.savefig('monthly_energy_carbon_trend.png', dpi=300)
  print('Saved: monthly_energy_carbon_trend.png')


def plot_waste_diversion_benchmark(df_facility: pd.DataFrame):
  """Plots Facility Waste Diversion Rates against Corporate Benchmark Target."""
  plt.figure(figsize=(10, 5))

  palette = [
      '#2ca02c' if rate >= 80 else '#ff7f0e'
      for rate in df_facility['diversion_rate']
  ]
  bars = sns.barplot(
      data=df_facility,
      x='facility_name',
      y='diversion_rate',
      palette=palette,
      hue='facility_name',
      legend=False,
  )

  # Add benchmark target line
  plt.axhline(
      y=80.0,
      color='red',
      linestyle='--',
      linewidth=2,
      label='Corporate Target (80%)',
  )

  # Annotate values on top of bars
  for bar in bars.patches:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 1.0,
        f'{height:.1f}%',
        ha='center',
        va='bottom',
        fontweight='bold',
    )

  plt.title(
      'Facility Waste Diversion Rate Benchmarking (%)',
      fontsize=14,
      fontweight='bold',
      pad=15,
  )
  plt.xlabel('Facility Name', fontweight='bold')
  plt.ylabel('Waste Diversion Rate (%)', fontweight='bold')
  plt.ylim(0, 100)
  plt.legend(loc='upper right')
  plt.tight_layout()
  plt.savefig('facility_waste_diversion.png', dpi=300)
  print('Saved: facility_waste_diversion.png')


if __name__ == '__main__':
  print('Initializing Sustainability Visualization Pipeline...')
  df_monthly, df_facility = generate_sample_data()
  plot_energy_carbon_trend(df_monthly)
  plot_waste_diversion_benchmark(df_facility)
  print('Dashboard chart generation complete.')
  

"""
CH7-Section5: 複数グラフとエクスポート
画像生成スクリプト
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import random
import os

# 出力ディレクトリ
output_dir = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(output_dir, exist_ok=True)

random.seed(42)

# ============================================
# 技術説明用
# ============================================

def tech_1row_3col():
    """1行3列のレイアウト"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 20]

    axes[0].plot(x, y, 'r-o')
    axes[0].set_title('Chart 1')

    axes[1].bar(x, y, color='steelblue')
    axes[1].set_title('Chart 2')

    axes[2].scatter(x, y, s=100, c='green')
    axes[2].set_title('Chart 3')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tech_1row_3col.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: tech_1row_3col.png")


def tech_gridspec():
    """GridSpec による不均等レイアウト"""
    fig = plt.figure(figsize=(12, 8))
    gs = gridspec.GridSpec(2, 2, height_ratios=[2, 1])

    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot([1, 2, 3, 4, 5], [10, 25, 20, 35, 30], 'b-o', linewidth=2)
    ax1.set_title('Main Chart (Full Width)', fontsize=14)
    ax1.grid(True, alpha=0.3)

    ax2 = fig.add_subplot(gs[1, 0])
    ax2.bar(['A', 'B', 'C'], [20, 30, 25], color='orange')
    ax2.set_title('Chart 2')

    ax3 = fig.add_subplot(gs[1, 1])
    ax3.scatter([1, 2, 3], [10, 20, 15], s=100, c='green')
    ax3.set_title('Chart 3')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tech_gridspec.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: tech_gridspec.png")


def tech_size_ratio():
    """サイズ比の調整"""
    fig = plt.figure(figsize=(12, 8))
    gs = gridspec.GridSpec(2, 3, width_ratios=[2, 1, 1], height_ratios=[1, 2])

    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot([1, 2, 3], [1, 2, 3], 'b-o')
    ax1.set_title('Wide')

    ax2 = fig.add_subplot(gs[0, 1])
    ax2.bar([1, 2], [1, 2], color='orange')
    ax2.set_title('Narrow 1')

    ax3 = fig.add_subplot(gs[0, 2])
    ax3.scatter([1, 2], [1, 2], s=80, c='green')
    ax3.set_title('Narrow 2')

    ax4 = fig.add_subplot(gs[1, :])
    ax4.bar(['A', 'B', 'C', 'D', 'E'], [5, 4, 3, 2, 1], color='steelblue')
    ax4.set_title('Full Width (Tall)')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tech_size_ratio.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: tech_size_ratio.png")


def tech_sharex():
    """x軸を共有"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    sales = [100, 120, 110, 130, 150]
    profit = [20, 25, 22, 28, 35]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(months, sales, 'b-o', linewidth=2)
    ax1.set_ylabel('Sales', fontsize=12)
    ax1.set_title('Sales and Profit Trend', fontsize=14)
    ax1.grid(True, alpha=0.3)

    ax2.plot(months, profit, 'g-s', linewidth=2)
    ax2.set_ylabel('Profit', fontsize=12)
    ax2.set_xlabel('Month', fontsize=12)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tech_sharex.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: tech_sharex.png")


def tech_sharey():
    """y軸を共有"""
    categories = ['A', 'B', 'C', 'D']
    values_2023 = [100, 80, 120, 90]
    values_2024 = [120, 95, 130, 110]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    ax1.bar(categories, values_2023, color='steelblue')
    ax1.set_title('2023', fontsize=14)
    ax1.set_ylabel('Value', fontsize=12)

    ax2.bar(categories, values_2024, color='coral')
    ax2.set_title('2024', fontsize=14)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tech_sharey.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: tech_sharey.png")


def tech_inset():
    """図の中に図を挿入"""
    x = list(range(1, 13))
    y = [10, 12, 15, 18, 22, 25, 28, 30, 27, 23, 18, 14]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, y, 'b-o', linewidth=2, markersize=8)
    ax.set_title('Annual Temperature Trend', fontsize=14)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Temperature (C)', fontsize=12)
    ax.grid(True, alpha=0.3)

    axins = inset_axes(ax, width="40%", height="40%", loc='upper right')
    axins.plot(x[4:9], y[4:9], 'r-o', linewidth=2, markersize=8)
    axins.set_title('Summer Detail', fontsize=10)
    axins.set_xlim(5, 9)
    axins.set_ylim(20, 32)
    axins.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tech_inset.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: tech_inset.png")


def tech_twinx():
    """双軸グラフ"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    sales = [100, 120, 115, 135, 150]
    profit_rate = [15, 18, 17, 22, 25]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color1 = 'steelblue'
    ax1.bar(months, sales, color=color1, alpha=0.7, label='Sales')
    ax1.set_xlabel('Month', fontsize=12)
    ax1.set_ylabel('Sales (10,000 yen)', color=color1, fontsize=12)
    ax1.tick_params(axis='y', labelcolor=color1)

    ax2 = ax1.twinx()
    color2 = 'coral'
    ax2.plot(months, profit_rate, 'o-', color=color2, linewidth=2, markersize=8, label='Profit Rate')
    ax2.set_ylabel('Profit Rate (%)', color=color2, fontsize=12)
    ax2.tick_params(axis='y', labelcolor=color2)

    plt.title('Sales and Profit Rate', fontsize=14, fontweight='bold')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tech_twinx.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: tech_twinx.png")


def tech_analysis_report():
    """実践：分析レポート"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [100, 115, 108, 130, 145, 160]
    target = [105, 110, 115, 120, 130, 145]
    profit_rate = [12, 14, 13, 16, 18, 20]

    products = ['Product A', 'Product B', 'Product C', 'Product D']
    product_sales = [40, 28, 20, 12]

    regions = ['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka']
    region_sales = [
        [random.gauss(100, 15) for _ in range(20)],
        [random.gauss(80, 12) for _ in range(20)],
        [random.gauss(70, 10) for _ in range(20)],
        [random.gauss(60, 8) for _ in range(20)]
    ]

    fig = plt.figure(figsize=(16, 12))
    gs = gridspec.GridSpec(3, 2, height_ratios=[1.5, 1, 1])

    # 上段
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(months, sales, 'o-', color='#3498db', linewidth=2.5, markersize=10, label='Actual Sales')
    ax1.plot(months, target, 's--', color='#e74c3c', linewidth=2, markersize=8, label='Target')

    ax1_twin = ax1.twinx()
    ax1_twin.fill_between(months, profit_rate, alpha=0.3, color='#2ecc71')
    ax1_twin.plot(months, profit_rate, '^-', color='#27ae60', linewidth=2, markersize=8, label='Profit Rate')
    ax1_twin.set_ylabel('Profit Rate (%)', color='#27ae60', fontsize=12)
    ax1_twin.tick_params(axis='y', labelcolor='#27ae60')

    ax1.set_title('Sales Performance Overview', fontsize=16, fontweight='bold')
    ax1.set_xlabel('Month', fontsize=12)
    ax1.set_ylabel('Sales (10,000 yen)', fontsize=12)
    ax1.legend(loc='upper left', fontsize=10)
    ax1_twin.legend(loc='upper right', fontsize=10)
    ax1.grid(True, axis='y', alpha=0.3)
    ax1.spines['top'].set_visible(False)

    # 中段左
    ax2 = fig.add_subplot(gs[1, 0])
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    ax2.pie(product_sales, labels=products, autopct='%1.1f%%', startangle=90, colors=colors,
            wedgeprops={'edgecolor': 'white', 'linewidth': 2})
    ax2.set_title('Sales by Product', fontsize=14, fontweight='bold')

    # 中段右
    ax3 = fig.add_subplot(gs[1, 1])
    bp = ax3.boxplot(region_sales, labels=regions, patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax3.set_title('Sales Distribution by Region', fontsize=14, fontweight='bold')
    ax3.set_ylabel('Sales', fontsize=12)
    ax3.grid(True, axis='y', alpha=0.3)

    # 下段左
    ax4 = fig.add_subplot(gs[2, 0])
    achievement = [s/t*100 for s, t in zip(sales, target)]
    bars = ax4.bar(months, achievement, color=['#27ae60' if a >= 100 else '#e74c3c' for a in achievement])
    ax4.axhline(y=100, color='gray', linestyle='--', linewidth=1)
    ax4.set_title('Target Achievement Rate', fontsize=14, fontweight='bold')
    ax4.set_ylabel('Achievement (%)', fontsize=12)
    ax4.set_ylim(80, 120)

    for bar, val in zip(bars, achievement):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{val:.1f}%', ha='center', fontsize=9)

    # 下段右
    ax5 = fig.add_subplot(gs[2, 1])
    region_totals = [sum(r) for r in region_sales]
    bars = ax5.barh(regions, region_totals, color=colors, edgecolor='white')
    ax5.set_title('Total Sales by Region', fontsize=14, fontweight='bold')
    ax5.set_xlabel('Total Sales', fontsize=12)

    for bar, val in zip(bars, region_totals):
        ax5.text(val + 20, bar.get_y() + bar.get_height()/2, f'{val:.0f}', va='center', fontsize=10)

    fig.suptitle('Sales Analysis Report - Q2 2024', fontsize=20, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    plt.savefig(os.path.join(output_dir, 'tech_analysis_report.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: tech_analysis_report.png")


# ============================================
# 演習用
# ============================================

def exercise_1_2x2():
    """演習1: 2x2グリッド"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    axes[0, 0].plot(x, y, 'b-o')
    axes[0, 0].set_title('Line Chart')

    axes[0, 1].bar(x, y, color='orange')
    axes[0, 1].set_title('Bar Chart')

    axes[1, 0].scatter(x, y, s=100, c='green')
    axes[1, 0].set_title('Scatter Plot')

    axes[1, 1].hist(y, bins=5, color='purple', edgecolor='black')
    axes[1, 1].set_title('Histogram')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'exercise_1_2x2.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_1_2x2.png")


def exercise_2_1x3():
    """演習2: 1行3列"""
    categories = ['A', 'B', 'C', 'D']
    values1 = [10, 20, 15, 25]
    values2 = [15, 25, 20, 30]
    values3 = [12, 22, 18, 28]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].bar(categories, values1, color='steelblue')
    axes[0].set_title('2022')
    axes[0].set_ylabel('Sales')

    axes[1].bar(categories, values2, color='coral')
    axes[1].set_title('2023')

    axes[2].bar(categories, values3, color='seagreen')
    axes[2].set_title('2024')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'exercise_2_1x3.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_2_1x3.png")


def exercise_3_sharex():
    """演習3: x軸を共有"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [100, 120, 110, 140, 150, 160]
    profit = [15, 20, 18, 25, 28, 30]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(months, sales, 'b-o', linewidth=2, markersize=8)
    ax1.set_ylabel('Sales (10,000 yen)', fontsize=12)
    ax1.set_title('Sales and Profit Trend', fontsize=14)
    ax1.grid(True, alpha=0.3)

    ax2.plot(months, profit, 'g-s', linewidth=2, markersize=8)
    ax2.set_ylabel('Profit (10,000 yen)', fontsize=12)
    ax2.set_xlabel('Month', fontsize=12)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'exercise_3_sharex.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_3_sharex.png")


def exercise_4_sharey():
    """演習4: y軸を共有"""
    categories = ['A', 'B', 'C', 'D']
    values_2023 = [80, 100, 90, 120]
    values_2024 = [90, 110, 100, 130]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    ax1.bar(categories, values_2023, color='steelblue')
    ax1.set_title('2023', fontsize=14)
    ax1.set_ylabel('Sales', fontsize=12)

    ax2.bar(categories, values_2024, color='coral')
    ax2.set_title('2024', fontsize=14)

    fig.suptitle('Year-over-Year Comparison', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    plt.savefig(os.path.join(output_dir, 'exercise_4_sharey.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_4_sharey.png")


def exercise_5_twinx():
    """演習5: 双軸グラフ"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    sales = [100, 120, 110, 130, 150]
    profit_rate = [10, 12, 11, 14, 16]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color1 = 'steelblue'
    ax1.bar(months, sales, color=color1, alpha=0.7, label='Sales')
    ax1.set_xlabel('Month', fontsize=12)
    ax1.set_ylabel('Sales (10,000 yen)', color=color1, fontsize=12)
    ax1.tick_params(axis='y', labelcolor=color1)

    ax2 = ax1.twinx()
    color2 = 'coral'
    ax2.plot(months, profit_rate, 'o-', color=color2, linewidth=2, markersize=8, label='Profit Rate')
    ax2.set_ylabel('Profit Rate (%)', color=color2, fontsize=12)
    ax2.tick_params(axis='y', labelcolor=color2)

    plt.title('Sales and Profit Rate', fontsize=14, fontweight='bold')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'exercise_5_twinx.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_5_twinx.png")


def exercise_6_png():
    """演習6: PNG保存"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-o', linewidth=2)
    plt.title('Sample Chart')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, alpha=0.3)

    plt.savefig(os.path.join(output_dir, 'exercise_6_png.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_6_png.png")


def exercise_7_multi_format():
    """演習7: 複数形式"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'b-o', linewidth=2)
    ax.set_title('Multi-Format Export')

    plt.savefig(os.path.join(output_dir, 'exercise_7_multi.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_7_multi.png")


def exercise_8_gridspec():
    """演習8: GridSpec"""
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 20]

    fig = plt.figure(figsize=(12, 8))
    gs = gridspec.GridSpec(2, 2, height_ratios=[2, 1])

    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(x, y, 'b-o', linewidth=2)
    ax1.set_title('Main Chart (Full Width)', fontsize=14)

    ax2 = fig.add_subplot(gs[1, 0])
    ax2.bar(x, y, color='orange')
    ax2.set_title('Sub Chart 1')

    ax3 = fig.add_subplot(gs[1, 1])
    ax3.scatter(x, y, s=100, c='green')
    ax3.set_title('Sub Chart 2')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'exercise_8_gridspec.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_8_gridspec.png")


# ============================================
# 応用問題用
# ============================================

def app_dashboard():
    """応用問題1: 売上分析ダッシュボード"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [100, 120, 110, 140, 155, 170]
    target = [110, 115, 120, 130, 145, 160]
    profit = [15, 18, 16, 22, 25, 28]

    products = ['A', 'B', 'C', 'D']
    product_sales = [40, 30, 20, 10]
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 左上
    ax1 = axes[0, 0]
    ax1.plot(months, sales, 'o-', color='#3498db', linewidth=2, markersize=8, label='Actual')
    ax1.plot(months, target, 's--', color='#e74c3c', linewidth=2, markersize=6, label='Target')
    ax1.set_title('Sales vs Target', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Sales (10,000 yen)')
    ax1.legend(loc='upper left')
    ax1.grid(True, axis='y', alpha=0.3)

    # 右上
    ax2 = axes[0, 1]
    ax2.bar(products, product_sales, color=colors, edgecolor='white')
    ax2.set_title('Sales by Product', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Sales (10,000 yen)')
    ax2.grid(True, axis='y', alpha=0.3)
    for i, v in enumerate(product_sales):
        ax2.text(i, v + 1, str(v), ha='center', fontsize=10)

    # 左下
    ax3 = axes[1, 0]
    ax3.pie(product_sales, labels=products, autopct='%1.1f%%', colors=colors, startangle=90,
            wedgeprops={'edgecolor': 'white', 'linewidth': 2})
    ax3.set_title('Product Share', fontsize=12, fontweight='bold')

    # 右下
    ax4 = axes[1, 1]
    ax4.bar(months, sales, color='#3498db', alpha=0.7, label='Sales')
    ax4.set_ylabel('Sales (10,000 yen)', color='#3498db')
    ax4.tick_params(axis='y', labelcolor='#3498db')

    ax4_twin = ax4.twinx()
    ax4_twin.plot(months, profit, 'o-', color='#e74c3c', linewidth=2, markersize=8, label='Profit')
    ax4_twin.set_ylabel('Profit (10,000 yen)', color='#e74c3c')
    ax4_twin.tick_params(axis='y', labelcolor='#e74c3c')
    ax4.set_title('Sales & Profit', fontsize=12, fontweight='bold')
    lines1, labels1 = ax4.get_legend_handles_labels()
    lines2, labels2 = ax4_twin.get_legend_handles_labels()
    ax4.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    fig.suptitle('Sales Dashboard - H1 2024', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    plt.savefig(os.path.join(output_dir, 'app_dashboard.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_dashboard.png")


def app_timeseries():
    """応用問題2: 時系列比較ダッシュボード"""
    dates = [f'Day {i}' for i in range(1, 15)]
    visitors = [random.randint(80, 150) for _ in range(14)]
    sales = [v * random.uniform(0.5, 0.8) for v in visitors]
    conversion = [s / v * 100 for s, v in zip(sales, visitors)]

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10), sharex=True)

    ax1.bar(dates, visitors, color='#3498db', alpha=0.8)
    ax1.set_ylabel('Visitors', fontsize=11)
    ax1.set_title('Daily Performance Metrics', fontsize=14, fontweight='bold')
    ax1.grid(True, axis='y', alpha=0.3)

    ax2.plot(dates, sales, 'o-', color='#27ae60', linewidth=2, markersize=6)
    ax2.set_ylabel('Sales', fontsize=11)
    ax2.grid(True, axis='y', alpha=0.3)
    ax2.fill_between(dates, sales, alpha=0.2, color='#27ae60')

    ax3.plot(dates, conversion, 's-', color='#e74c3c', linewidth=2, markersize=6)
    ax3.set_ylabel('Conversion Rate (%)', fontsize=11)
    ax3.set_xlabel('Date', fontsize=11)
    ax3.grid(True, axis='y', alpha=0.3)

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'app_timeseries.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_timeseries.png")


def app_uneven_layout():
    """応用問題3: 不均等レイアウト"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [100, 120, 110, 140, 155, 170]
    products = ['A', 'B', 'C']
    q1 = [30, 25, 20]
    q2 = [35, 28, 22]

    fig = plt.figure(figsize=(14, 10))
    gs = gridspec.GridSpec(2, 3, height_ratios=[2, 1])

    ax_main = fig.add_subplot(gs[0, :])
    ax_main.plot(months, sales, 'o-', color='#3498db', linewidth=3, markersize=12)
    ax_main.set_title('Monthly Sales Trend (Main)', fontsize=14, fontweight='bold')
    ax_main.set_ylabel('Sales (10,000 yen)', fontsize=12)
    ax_main.grid(True, alpha=0.3)
    ax_main.set_ylim(80, 180)
    ax_main.annotate('Peak', xy=(5, 170), xytext=(4, 175),
                     fontsize=11, arrowprops=dict(arrowstyle='->', color='red'))

    ax1 = fig.add_subplot(gs[1, 0])
    ax1.bar(products, q1, color='#e74c3c')
    ax1.set_title('Q1 Sales', fontsize=12)
    ax1.set_ylabel('Sales')

    ax2 = fig.add_subplot(gs[1, 1])
    ax2.bar(products, q2, color='#27ae60')
    ax2.set_title('Q2 Sales', fontsize=12)

    ax3 = fig.add_subplot(gs[1, 2])
    total = [sum(x) for x in zip(q1, q2)]
    ax3.pie(total, labels=products, autopct='%1.0f%%', colors=['#3498db', '#e74c3c', '#f39c12'])
    ax3.set_title('Total Share', fontsize=12)

    fig.suptitle('Sales Analysis Dashboard', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    plt.savefig(os.path.join(output_dir, 'app_uneven_layout.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_uneven_layout.png")


def app_batch_export():
    """応用問題4: バッチエクスポート"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [100, 120, 110, 140, 155, 170]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(months, sales, 'o-', color='#3498db', linewidth=2.5, markersize=10,
            markeredgecolor='white', markeredgewidth=2)
    ax.set_title('Monthly Sales Report - H1 2024', fontsize=14, fontweight='bold')
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Sales (10,000 yen)', fontsize=12)
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'app_batch_export.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_batch_export.png")


def app_full_report():
    """応用問題5: 総合レポート"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    revenue = [1000, 1200, 1100, 1400, 1550, 1700]
    cost = [600, 700, 680, 800, 850, 900]
    profit = [r - c for r, c in zip(revenue, cost)]
    profit_margin = [p / r * 100 for p, r in zip(profit, revenue)]

    products = ['Product A', 'Product B', 'Product C', 'Product D']
    product_revenue = [500, 350, 250, 100]

    regions = ['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka']
    region_data = [[random.gauss(m, 10) for _ in range(12)] for m in [100, 80, 70, 60]]

    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

    fig = plt.figure(figsize=(16, 14))
    gs = gridspec.GridSpec(3, 2, height_ratios=[1.5, 1, 1])

    # 上段
    ax1 = fig.add_subplot(gs[0, :])
    x = range(len(months))
    width = 0.35
    ax1.bar([i - width/2 for i in x], revenue, width, label='Revenue', color=colors[0], alpha=0.8)
    ax1.bar([i + width/2 for i in x], cost, width, label='Cost', color=colors[1], alpha=0.8)
    ax1.set_ylabel('Amount (10,000 yen)', fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(months)
    ax1.legend(loc='upper left')
    ax1.grid(True, axis='y', alpha=0.3)

    ax1_twin = ax1.twinx()
    ax1_twin.plot(x, profit, 'o-', color=colors[2], linewidth=2.5, markersize=10, label='Profit')
    ax1_twin.set_ylabel('Profit (10,000 yen)', color=colors[2], fontsize=11)
    ax1_twin.tick_params(axis='y', labelcolor=colors[2])
    ax1_twin.legend(loc='upper right')
    ax1.set_title('Revenue, Cost and Profit Trend', fontsize=14, fontweight='bold')

    # 左中段
    ax2 = fig.add_subplot(gs[1, 0])
    bars = ax2.barh(products, product_revenue, color=colors, edgecolor='white')
    ax2.set_xlabel('Revenue (10,000 yen)', fontsize=11)
    ax2.set_title('Revenue by Product', fontsize=12, fontweight='bold')
    ax2.grid(True, axis='x', alpha=0.3)
    for bar, val in zip(bars, product_revenue):
        ax2.text(val + 10, bar.get_y() + bar.get_height()/2, f'{val}', va='center', fontsize=10)

    # 右中段
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.pie(product_revenue, labels=products, autopct='%1.1f%%', colors=colors, startangle=90,
            wedgeprops={'edgecolor': 'white', 'linewidth': 2})
    ax3.set_title('Product Share', fontsize=12, fontweight='bold')

    # 左下段
    ax4 = fig.add_subplot(gs[2, 0])
    ax4.fill_between(months, profit_margin, alpha=0.5, color=colors[2])
    ax4.plot(months, profit_margin, 'o-', color=colors[2], linewidth=2)
    ax4.set_xlabel('Month', fontsize=11)
    ax4.set_ylabel('Profit Margin (%)', fontsize=11)
    ax4.set_title('Profit Margin Trend', fontsize=12, fontweight='bold')
    ax4.set_ylim(30, 50)
    ax4.grid(True, alpha=0.3)

    # 右下段
    ax5 = fig.add_subplot(gs[2, 1])
    bp = ax5.boxplot(region_data, labels=regions, patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax5.set_xlabel('Region', fontsize=11)
    ax5.set_ylabel('Sales', fontsize=11)
    ax5.set_title('Sales Distribution by Region', fontsize=12, fontweight='bold')
    ax5.grid(True, axis='y', alpha=0.3)

    fig.suptitle('Business Analysis Report - H1 2024', fontsize=18, fontweight='bold', y=0.99)
    plt.tight_layout()
    plt.subplots_adjust(top=0.94, hspace=0.3, wspace=0.25)
    plt.savefig(os.path.join(output_dir, 'app_full_report.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_full_report.png")


# ============================================
# メイン
# ============================================

if __name__ == '__main__':
    print("Generating Section5 images...")
    
    # 技術説明
    tech_1row_3col()
    tech_gridspec()
    tech_size_ratio()
    tech_sharex()
    tech_sharey()
    tech_inset()
    tech_twinx()
    tech_analysis_report()
    
    # 演習
    exercise_1_2x2()
    exercise_2_1x3()
    exercise_3_sharex()
    exercise_4_sharey()
    exercise_5_twinx()
    exercise_6_png()
    exercise_7_multi_format()
    exercise_8_gridspec()
    
    # 応用問題
    app_dashboard()
    app_timeseries()
    app_uneven_layout()
    app_batch_export()
    app_full_report()
    
    print(f"\nAll images saved to: {output_dir}")

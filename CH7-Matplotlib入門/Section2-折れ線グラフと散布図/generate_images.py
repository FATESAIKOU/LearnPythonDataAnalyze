#!/usr/bin/env python3
"""
CH7-Section2 用の画像を生成するスクリプト
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import os
import random

output_dir = os.path.dirname(os.path.abspath(__file__)) + "/images"
os.makedirs(output_dir, exist_ok=True)

# =============================================================================
# 技術説明用の画像
# =============================================================================

# 1. 線のスタイル (tech_line_styles.png)
def generate_tech_line_styles():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 20]
    
    fig, axes = plt.subplots(1, 4, figsize=(14, 4))
    
    styles = ['-', '--', ':', '-.']
    titles = ["Solid '-'", "Dashed '--'", "Dotted ':'", "Dash-dot '-.'"]
    
    for ax, style, title in zip(axes, styles, titles):
        ax.plot(x, y, linestyle=style, linewidth=2, marker='o', markersize=8)
        ax.set_title(title, fontsize=12)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_line_styles.png", dpi=150)
    plt.close()
    print("Generated: tech_line_styles.png")

# 2. scatter() の基本 (tech_scatter_basic.png)
def generate_tech_scatter_basic():
    ad_cost = [10, 20, 30, 40, 50, 60, 70, 80]
    sales = [15, 25, 40, 45, 60, 70, 75, 90]
    
    plt.figure(figsize=(8, 5))
    plt.scatter(ad_cost, sales, s=80, alpha=0.7)
    plt.xlabel("Ad Cost", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.title("Ad Cost vs Sales", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_scatter_basic.png", dpi=150)
    plt.close()
    print("Generated: tech_scatter_basic.png")

# 3. 点のサイズや色を変える (tech_scatter_size_color.png)
def generate_tech_scatter_size_color():
    x = [10, 20, 30, 40, 50]
    y = [15, 30, 40, 55, 70]
    sizes = [100, 200, 300, 400, 500]
    colors = [1, 2, 3, 4, 5]
    
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7, edgecolor='black')
    plt.colorbar(scatter, label='Value')
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Y", fontsize=12)
    plt.title("Scatter with Variable Size and Color", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_scatter_size_color.png", dpi=150)
    plt.close()
    print("Generated: tech_scatter_size_color.png")

# 4. 正の相関・負の相関 (tech_correlation.png)
def generate_tech_correlation():
    random.seed(42)
    
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    
    # 正の相関
    x = list(range(1, 21))
    y_pos = [i * 2 + random.randint(-5, 5) for i in x]
    axes[0].scatter(x, y_pos, s=60, alpha=0.7, color='blue')
    axes[0].set_title("Positive Correlation", fontsize=12)
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    axes[0].grid(True, alpha=0.3)
    
    # 負の相関
    y_neg = [40 - i * 1.5 + random.randint(-5, 5) for i in x]
    axes[1].scatter(x, y_neg, s=60, alpha=0.7, color='red')
    axes[1].set_title("Negative Correlation", fontsize=12)
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("y")
    axes[1].grid(True, alpha=0.3)
    
    # 相関なし
    y_none = [random.randint(10, 40) for _ in x]
    axes[2].scatter(x, y_none, s=60, alpha=0.7, color='green')
    axes[2].set_title("No Correlation", fontsize=12)
    axes[2].set_xlabel("x")
    axes[2].set_ylabel("y")
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_correlation.png", dpi=150)
    plt.close()
    print("Generated: tech_correlation.png")

# 5. 実践：売上分析グラフ (tech_sales_analysis.png)
def generate_tech_sales_analysis():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales_2023 = [100, 120, 90, 130, 150, 140]
    sales_2024 = [110, 140, 100, 150, 180, 170]
    ad_cost = [10, 15, 12, 18, 25, 22]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # 折れ線グラフ
    axes[0].plot(months, sales_2023, 'b-o', label='2023', linewidth=2, markersize=8)
    axes[0].plot(months, sales_2024, 'r--s', label='2024', linewidth=2, markersize=8)
    axes[0].set_title("Monthly Sales Comparison", fontsize=14)
    axes[0].set_xlabel("Month", fontsize=12)
    axes[0].set_ylabel("Sales", fontsize=12)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # 散布図
    axes[1].scatter(ad_cost, sales_2024, s=100, c='red', alpha=0.7, edgecolor='black')
    axes[1].set_title("Ad Cost vs Sales (2024)", fontsize=14)
    axes[1].set_xlabel("Ad Cost", fontsize=12)
    axes[1].set_ylabel("Sales", fontsize=12)
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_sales_analysis.png", dpi=150)
    plt.close()
    print("Generated: tech_sales_analysis.png")

# =============================================================================
# 演習用の画像
# =============================================================================

# 6. 演習1: 線のスタイル (exercise_1_dashed.png)
def generate_exercise_1_dashed():
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, linestyle='--', linewidth=2, marker='o', markersize=8)
    plt.title("Dashed Line", fontsize=14)
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Y", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_1_dashed.png", dpi=150)
    plt.close()
    print("Generated: exercise_1_dashed.png")

# 7. 演習2: マーカーを追加 (exercise_2_marker.png)
def generate_exercise_2_marker():
    x = [1, 2, 3, 4, 5]
    y = [5, 15, 10, 20, 18]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linewidth=2, markersize=8)
    plt.title("Line with Markers", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_2_marker.png", dpi=150)
    plt.close()
    print("Generated: exercise_2_marker.png")

# 8. 演習5: 基本の散布図 (exercise_5_scatter.png)
def generate_exercise_5_scatter():
    study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
    test_score = [40, 50, 55, 60, 70, 75, 85, 90]
    
    plt.figure(figsize=(8, 5))
    plt.scatter(study_hours, test_score, s=80, alpha=0.7)
    plt.title("Study Hours vs Test Score", fontsize=14)
    plt.xlabel("Study Hours", fontsize=12)
    plt.ylabel("Test Score", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_5_scatter.png", dpi=150)
    plt.close()
    print("Generated: exercise_5_scatter.png")

# =============================================================================
# 応用問題用の画像
# =============================================================================

# 9. 応用問題1: 株価チャート (app_stock_chart.png)
def generate_app_stock_chart():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    stock_a = [1000, 1050, 980, 1100, 1080]
    stock_b = [500, 520, 480, 550, 530]
    
    plt.figure(figsize=(10, 6))
    plt.plot(days, stock_a, 'ro-', label='Stock A', linewidth=2, markersize=8)
    plt.plot(days, stock_b, 'bs--', label='Stock B', linewidth=2, markersize=8)
    
    plt.title("Stock Price Comparison", fontsize=14)
    plt.xlabel("Day", fontsize=12)
    plt.ylabel("Price (Yen)", fontsize=12)
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_stock_chart.png", dpi=150)
    plt.close()
    print("Generated: app_stock_chart.png")

# 10. 応用問題2: 相関分析散布図 (app_height_weight.png)
def generate_app_height_weight():
    height = [155, 160, 162, 168, 170, 172, 175, 178, 180, 185]
    weight = [50, 52, 55, 60, 63, 65, 70, 72, 75, 80]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(height, weight, s=100, c='green', alpha=0.7, edgecolor='black')
    
    plt.title("Height vs Weight", fontsize=14)
    plt.xlabel("Height (cm)", fontsize=12)
    plt.ylabel("Weight (kg)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_height_weight.png", dpi=150)
    plt.close()
    print("Generated: app_height_weight.png")

# 11. 応用問題3: 年度別売上トレンド (app_sales_trend.png)
def generate_app_sales_trend():
    months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]
    sales_2022 = [80, 90, 85, 100, 110, 95]
    sales_2023 = [90, 100, 95, 115, 125, 110]
    sales_2024 = [100, 120, 110, 130, 145, 125]
    
    plt.figure(figsize=(12, 6))
    plt.plot(months, sales_2022, 'g:^', label='2022', linewidth=2, markersize=8)
    plt.plot(months, sales_2023, 'b--s', label='2023', linewidth=2, markersize=8)
    plt.plot(months, sales_2024, 'r-o', label='2024', linewidth=2, markersize=8)
    
    plt.title("Monthly Sales Trend", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.ylim(70, 160)
    plt.legend(loc='lower right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_sales_trend.png", dpi=150)
    plt.close()
    print("Generated: app_sales_trend.png")

# 12. 応用問題4: バブルチャート (app_bubble_chart.png)
def generate_app_bubble_chart():
    stores = ["A", "B", "C", "D", "E", "F"]
    ad_cost = [10, 25, 15, 40, 30, 50]
    visitors = [100, 200, 150, 350, 280, 400]
    sales = [30, 60, 45, 100, 80, 120]
    
    sizes = [s * 5 for s in sales]
    
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(ad_cost, visitors, s=sizes, c=sales, 
                          cmap='YlOrRd', alpha=0.6, edgecolor='black')
    plt.colorbar(scatter, label='Sales')
    
    plt.title("Ad Cost vs Visitors (Bubble = Sales)", fontsize=14)
    plt.xlabel("Ad Cost", fontsize=12)
    plt.ylabel("Visitors", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_bubble_chart.png", dpi=150)
    plt.close()
    print("Generated: app_bubble_chart.png")

# =============================================================================
# すべての画像を生成
# =============================================================================

if __name__ == "__main__":
    print("Generating images for CH7-Section2...")
    print("=" * 50)
    
    # 技術説明
    generate_tech_line_styles()
    generate_tech_scatter_basic()
    generate_tech_scatter_size_color()
    generate_tech_correlation()
    generate_tech_sales_analysis()
    
    # 演習
    generate_exercise_1_dashed()
    generate_exercise_2_marker()
    generate_exercise_5_scatter()
    
    # 応用問題
    generate_app_stock_chart()
    generate_app_height_weight()
    generate_app_sales_trend()
    generate_app_bubble_chart()
    
    print("=" * 50)
    print("All images generated successfully!")
    print(f"Output directory: {output_dir}")

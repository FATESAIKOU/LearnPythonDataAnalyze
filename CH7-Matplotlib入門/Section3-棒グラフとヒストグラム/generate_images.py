#!/usr/bin/env python3
"""
CH7-Section3 用の画像を生成するスクリプト
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import numpy as np
import random
import os

output_dir = os.path.dirname(os.path.abspath(__file__)) + "/images"
os.makedirs(output_dir, exist_ok=True)

# =============================================================================
# 技術説明用の画像
# =============================================================================

# 1. 縦棒グラフ (tech_bar_vertical.png)
def generate_tech_bar_vertical():
    categories = ["Tokyo", "Osaka", "Nagoya"]
    values = [100, 120, 80]
    
    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color='steelblue', edgecolor='black', width=0.6, alpha=0.8)
    plt.title("Sales by City", fontsize=14)
    plt.xlabel("City", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_bar_vertical.png", dpi=150)
    plt.close()
    print("Generated: tech_bar_vertical.png")

# 2. 横棒グラフ (tech_bar_horizontal.png)
def generate_tech_bar_horizontal():
    categories = ["Tokyo", "Osaka", "Nagoya"]
    values = [100, 120, 80]
    
    plt.figure(figsize=(8, 5))
    plt.barh(categories, values, color='coral', edgecolor='black')
    plt.title("Sales by City", fontsize=14)
    plt.xlabel("Sales", fontsize=12)
    plt.ylabel("City", fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_bar_horizontal.png", dpi=150)
    plt.close()
    print("Generated: tech_bar_horizontal.png")

# 3. グループ化棒グラフ (tech_bar_grouped.png)
def generate_tech_bar_grouped():
    categories = ["Tokyo", "Osaka", "Nagoya"]
    values_2023 = [100, 110, 70]
    values_2024 = [80, 120, 80]
    
    x = np.arange(len(categories))
    width = 0.35
    
    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, values_2023, width, label='2023', color='steelblue')
    plt.bar(x + width/2, values_2024, width, label='2024', color='coral')
    
    plt.xlabel("City", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.title("Sales Comparison by Year", fontsize=14)
    plt.xticks(x, categories)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_bar_grouped.png", dpi=150)
    plt.close()
    print("Generated: tech_bar_grouped.png")

# 4. 積み上げ棒グラフ (tech_bar_stacked.png)
def generate_tech_bar_stacked():
    categories = ["Tokyo", "Osaka", "Nagoya"]
    q1_sales = [100, 110, 70]
    q2_sales = [80, 90, 80]
    
    plt.figure(figsize=(10, 6))
    plt.bar(categories, q1_sales, label='Q1', color='steelblue')
    plt.bar(categories, q2_sales, bottom=q1_sales, label='Q2', color='coral')
    
    plt.xlabel("City", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.title("Quarterly Sales (Stacked)", fontsize=14)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_bar_stacked.png", dpi=150)
    plt.close()
    print("Generated: tech_bar_stacked.png")

# 5. 棒グラフとヒストグラムの違い (tech_bar_vs_hist.png)
def generate_tech_bar_vs_hist():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 棒グラフ（カテゴリ比較）
    categories = ["A", "B", "C"]
    values = [30, 50, 40]
    ax1.bar(categories, values, color='steelblue', edgecolor='black')
    ax1.set_title("Bar Chart (Categories)", fontsize=14)
    ax1.set_xlabel("Category", fontsize=12)
    ax1.set_ylabel("Value", fontsize=12)
    ax1.grid(axis='y', alpha=0.3)
    
    # ヒストグラム（分布）
    random.seed(42)
    scores = [random.gauss(75, 10) for _ in range(100)]
    ax2.hist(scores, bins=10, color='coral', edgecolor='black', alpha=0.7)
    ax2.set_title("Histogram (Distribution)", fontsize=14)
    ax2.set_xlabel("Value Range", fontsize=12)
    ax2.set_ylabel("Frequency", fontsize=12)
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_bar_vs_hist.png", dpi=150)
    plt.close()
    print("Generated: tech_bar_vs_hist.png")

# 6. 円グラフの基本 (tech_pie_basic.png)
def generate_tech_pie_basic():
    labels = ["Tokyo", "Osaka", "Nagoya"]
    values = [40, 35, 25]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors,
            wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    plt.title("Sales Share", fontsize=14)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_pie_basic.png", dpi=150)
    plt.close()
    print("Generated: tech_pie_basic.png")

# 7. 円グラフのイメージ (tech_pie_examples.png)
def generate_tech_pie_examples():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    
    # 2等分
    axes[0].pie([50, 50], labels=['A 50%', 'B 50%'], startangle=90, colors=colors[:2],
                wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    axes[0].set_title("2 Parts", fontsize=12)
    
    # 3等分
    axes[1].pie([33.3, 33.3, 33.4], labels=['A 33%', 'B 33%', 'C 33%'], startangle=90, 
                colors=colors[:3], wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    axes[1].set_title("3 Parts", fontsize=12)
    
    # 4等分
    axes[2].pie([25, 25, 25, 25], labels=['A 25%', 'B 25%', 'C 25%', 'D 25%'], startangle=90,
                colors=colors, wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    axes[2].set_title("4 Parts", fontsize=12)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_pie_examples.png", dpi=150)
    plt.close()
    print("Generated: tech_pie_examples.png")

# 8. 売上分析ダッシュボード (tech_dashboard.png)
def generate_tech_dashboard():
    random.seed(42)
    
    cities = ["Tokyo", "Osaka", "Nagoya", "Fukuoka"]
    sales_2023 = [100, 90, 70, 60]
    sales_2024 = [120, 95, 80, 75]
    
    tokyo_monthly = [random.gauss(100, 15) for _ in range(12)]
    osaka_monthly = [random.gauss(90, 12) for _ in range(12)]
    
    categories = ["Product A", "Product B", "Product C", "Other"]
    shares = [45, 25, 20, 10]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. グループ化棒グラフ
    ax1 = axes[0, 0]
    x = np.arange(len(cities))
    width = 0.35
    ax1.bar(x - width/2, sales_2023, width, label='2023', color='steelblue')
    ax1.bar(x + width/2, sales_2024, width, label='2024', color='coral')
    ax1.set_xlabel("City")
    ax1.set_ylabel("Sales")
    ax1.set_title("Sales by City (Year Comparison)")
    ax1.set_xticks(x)
    ax1.set_xticklabels(cities)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)
    
    # 2. ヒストグラム
    ax2 = axes[0, 1]
    ax2.hist(tokyo_monthly, bins=8, alpha=0.7, label='Tokyo', color='blue')
    ax2.hist(osaka_monthly, bins=8, alpha=0.7, label='Osaka', color='red')
    ax2.set_xlabel("Monthly Sales")
    ax2.set_ylabel("Frequency")
    ax2.set_title("Sales Distribution")
    ax2.legend()
    ax2.grid(axis='y', alpha=0.3)
    
    # 3. 円グラフ
    ax3 = axes[1, 0]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    ax3.pie(shares, labels=categories, autopct='%1.1f%%',
            startangle=90, colors=colors,
            wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    ax3.set_title("Sales by Product Category")
    
    # 4. 箱ひげ図
    ax4 = axes[1, 1]
    all_monthly = [tokyo_monthly, osaka_monthly]
    ax4.boxplot(all_monthly, labels=['Tokyo', 'Osaka'])
    ax4.set_xlabel("City")
    ax4.set_ylabel("Monthly Sales")
    ax4.set_title("Sales Variation by City")
    ax4.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_dashboard.png", dpi=150)
    plt.close()
    print("Generated: tech_dashboard.png")

# =============================================================================
# 演習用の画像
# =============================================================================

# 9. 演習1: 基本の棒グラフ (exercise_1_bar.png)
def generate_exercise_1_bar():
    products = ["Product A", "Product B", "Product C", "Product D"]
    sales = [150, 200, 120, 180]
    
    plt.figure(figsize=(8, 5))
    plt.bar(products, sales, color='steelblue', edgecolor='black')
    plt.title("Sales by Product", fontsize=14)
    plt.xlabel("Product", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_1_bar.png", dpi=150)
    plt.close()
    print("Generated: exercise_1_bar.png")

# 10. 演習3: 横棒グラフ (exercise_3_barh.png)
def generate_exercise_3_barh():
    stores = ["Shibuya", "Shinjuku", "Ikebukuro", "Tokyo", "Ueno"]
    visitors = [500, 450, 380, 420, 300]
    
    plt.figure(figsize=(8, 5))
    plt.barh(stores, visitors, color='coral', edgecolor='black')
    plt.title("Visitors by Store", fontsize=14)
    plt.xlabel("Visitors", fontsize=12)
    plt.ylabel("Store", fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_3_barh.png", dpi=150)
    plt.close()
    print("Generated: exercise_3_barh.png")

# 11. 演習4: 基本のヒストグラム (exercise_4_hist.png)
def generate_exercise_4_hist():
    scores = [55, 62, 68, 70, 72, 75, 77, 78, 80, 82,
              83, 85, 86, 87, 88, 89, 90, 91, 92, 93,
              94, 95, 65, 71, 76, 79, 81, 84, 88, 96]
    
    plt.figure(figsize=(8, 5))
    plt.hist(scores, color='skyblue', edgecolor='black')
    plt.title("Score Distribution", fontsize=14)
    plt.xlabel("Score", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_4_hist.png", dpi=150)
    plt.close()
    print("Generated: exercise_4_hist.png")

# 12. 演習5: ヒストグラムのビン数を変える (exercise_5_hist_bins.png)
def generate_exercise_5_hist_bins():
    scores = [55, 62, 68, 70, 72, 75, 77, 78, 80, 82,
              83, 85, 86, 87, 88, 89, 90, 91, 92, 93,
              94, 95, 65, 71, 76, 79, 81, 84, 88, 96]
    
    plt.figure(figsize=(8, 5))
    plt.hist(scores, bins=5, color='skyblue', edgecolor='black')
    plt.title("Score Distribution (bins=5)", fontsize=14)
    plt.xlabel("Score", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_5_hist_bins.png", dpi=150)
    plt.close()
    print("Generated: exercise_5_hist_bins.png")

# 13. 演習6: 基本の円グラフ (exercise_6_pie.png)
def generate_exercise_6_pie():
    categories = ["Food", "Drink", "Snack", "Other"]
    values = [45, 25, 20, 10]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=categories, colors=colors,
            wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    plt.title("Sales Share", fontsize=14)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_6_pie.png", dpi=150)
    plt.close()
    print("Generated: exercise_6_pie.png")

# 14. 演習7: 円グラフにパーセント (exercise_7_pie_pct.png)
def generate_exercise_7_pie_pct():
    categories = ["Food", "Drink", "Snack", "Other"]
    values = [45, 25, 20, 10]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=colors,
            wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    plt.title("Sales Share", fontsize=14)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_7_pie_pct.png", dpi=150)
    plt.close()
    print("Generated: exercise_7_pie_pct.png")

# 15. 演習8: 箱ひげ図 (exercise_8_boxplot.png)
def generate_exercise_8_boxplot():
    class_a = [65, 70, 72, 75, 78, 80, 82, 85, 88, 90]
    class_b = [60, 68, 75, 78, 80, 82, 85, 90, 95, 98]
    data = [class_a, class_b]
    
    plt.figure(figsize=(8, 5))
    plt.boxplot(data, labels=['Class A', 'Class B'])
    plt.title("Score Distribution by Class", fontsize=14)
    plt.ylabel("Score", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_8_boxplot.png", dpi=150)
    plt.close()
    print("Generated: exercise_8_boxplot.png")

# 16. 演習9: グループ化棒グラフ (exercise_9_grouped.png)
def generate_exercise_9_grouped():
    cities = ["Tokyo", "Osaka", "Nagoya"]
    sales_2023 = [100, 85, 70]
    sales_2024 = [120, 95, 80]
    
    x = np.arange(len(cities))
    width = 0.35
    
    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, sales_2023, width, label='2023', color='steelblue')
    plt.bar(x + width/2, sales_2024, width, label='2024', color='coral')
    plt.xticks(x, cities)
    plt.title("Sales by Year", fontsize=14)
    plt.ylabel("Sales", fontsize=12)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_9_grouped.png", dpi=150)
    plt.close()
    print("Generated: exercise_9_grouped.png")

# 17. 演習10: 積み上げ棒グラフ (exercise_10_stacked.png)
def generate_exercise_10_stacked():
    cities = ["Tokyo", "Osaka", "Nagoya"]
    q1 = [50, 45, 35]
    q2 = [60, 50, 40]
    
    plt.figure(figsize=(8, 5))
    plt.bar(cities, q1, label='Q1', color='steelblue')
    plt.bar(cities, q2, bottom=q1, label='Q2', color='coral')
    plt.title("Quarterly Sales (Stacked)", fontsize=14)
    plt.ylabel("Sales", fontsize=12)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_10_stacked.png", dpi=150)
    plt.close()
    print("Generated: exercise_10_stacked.png")

# =============================================================================
# 応用問題用の画像
# =============================================================================

# 18. 応用問題1: 月別売上比較 (app_monthly_sales.png)
def generate_app_monthly_sales():
    months = ["Jan", "Feb", "Mar"]
    tokyo = [100, 120, 110]
    osaka = [80, 95, 90]
    nagoya = [60, 70, 75]
    
    x = np.arange(len(months))
    width = 0.25
    
    plt.figure(figsize=(10, 6))
    plt.bar(x - width, tokyo, width, label='Tokyo', color='blue')
    plt.bar(x, osaka, width, label='Osaka', color='red')
    plt.bar(x + width, nagoya, width, label='Nagoya', color='green')
    
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.title("Monthly Sales by City", fontsize=14)
    plt.xticks(x, months)
    plt.legend(loc='upper right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_monthly_sales.png", dpi=150)
    plt.close()
    print("Generated: app_monthly_sales.png")

# 19. 応用問題2: 売上構成の可視化 (app_sales_breakdown.png)
def generate_app_sales_breakdown():
    categories = ["Food", "Drink", "Dessert", "Other"]
    tokyo = [50, 30, 15, 5]
    osaka = [45, 35, 12, 8]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 積み上げ棒グラフ
    cities = ['Tokyo', 'Osaka']
    bottom_t = 0
    bottom_o = 0
    for i, cat in enumerate(categories):
        ax1.bar(cities[0], tokyo[i], bottom=bottom_t, label=cat if i < 4 else '', color=colors[i])
        ax1.bar(cities[1], osaka[i], bottom=bottom_o, color=colors[i])
        bottom_t += tokyo[i]
        bottom_o += osaka[i]
    
    ax1.set_ylabel('Sales', fontsize=12)
    ax1.set_title('Sales Breakdown by City', fontsize=14)
    ax1.legend(loc='upper right')
    ax1.grid(axis='y', alpha=0.3)
    
    # 円グラフ
    ax2.pie(tokyo, labels=categories, autopct='%1.1f%%', startangle=90, colors=colors,
            wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    ax2.set_title('Tokyo Sales Share', fontsize=14)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_sales_breakdown.png", dpi=150)
    plt.close()
    print("Generated: app_sales_breakdown.png")

# 20. 応用問題3: 成績分布の分析 (app_score_analysis.png)
def generate_app_score_analysis():
    random.seed(42)
    
    class_a = [random.gauss(70, 12) for _ in range(40)]
    class_b = [random.gauss(75, 10) for _ in range(40)]
    class_c = [random.gauss(65, 15) for _ in range(40)]
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # ヒストグラム
    ax1.hist(class_a, bins=15, alpha=0.5, label='Class A', color='blue')
    ax1.hist(class_b, bins=15, alpha=0.5, label='Class B', color='red')
    ax1.hist(class_c, bins=15, alpha=0.5, label='Class C', color='green')
    ax1.set_xlabel('Score', fontsize=12)
    ax1.set_ylabel('Frequency', fontsize=12)
    ax1.set_title('Score Distribution (Histogram)', fontsize=14)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)
    
    # 箱ひげ図
    data = [class_a, class_b, class_c]
    ax2.boxplot(data, labels=['Class A', 'Class B', 'Class C'])
    ax2.set_xlabel('Class', fontsize=12)
    ax2.set_ylabel('Score', fontsize=12)
    ax2.set_title('Score Distribution (Box Plot)', fontsize=14)
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_score_analysis.png", dpi=150)
    plt.close()
    print("Generated: app_score_analysis.png")

# 21. 応用問題4: 売上ダッシュボード (app_sales_dashboard.png)
def generate_app_sales_dashboard():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [80, 95, 110, 105, 120, 130]
    
    products = ["A", "B", "C", "D"]
    product_sales = [40, 30, 20, 10]
    
    regions = ["East", "West", "North", "South"]
    region_sales = [35, 25, 22, 18]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 折れ線グラフ
    ax1 = axes[0, 0]
    ax1.plot(months, sales, 'bo-', linewidth=2, markersize=8)
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Sales')
    ax1.set_title('Monthly Sales Trend')
    ax1.grid(True, alpha=0.3)
    
    # 棒グラフ
    ax2 = axes[0, 1]
    ax2.bar(products, product_sales, color='steelblue', edgecolor='black')
    ax2.set_xlabel('Product')
    ax2.set_ylabel('Sales')
    ax2.set_title('Sales by Product')
    ax2.grid(axis='y', alpha=0.3)
    
    # 円グラフ
    ax3 = axes[1, 0]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    ax3.pie(region_sales, labels=regions, autopct='%1.1f%%', startangle=90, colors=colors,
            wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    ax3.set_title('Sales by Region')
    
    # ヒストグラム
    ax4 = axes[1, 1]
    ax4.hist(sales, bins=5, color='coral', edgecolor='black', alpha=0.7)
    ax4.set_xlabel('Sales')
    ax4.set_ylabel('Frequency')
    ax4.set_title('Sales Distribution')
    ax4.grid(axis='y', alpha=0.3)
    
    fig.suptitle('Sales Dashboard', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    plt.savefig(f"{output_dir}/app_sales_dashboard.png", dpi=150)
    plt.close()
    print("Generated: app_sales_dashboard.png")

# =============================================================================
# すべての画像を生成
# =============================================================================

if __name__ == "__main__":
    print("Generating images for CH7-Section3...")
    print("=" * 50)
    
    # 技術説明
    generate_tech_bar_vertical()
    generate_tech_bar_horizontal()
    generate_tech_bar_grouped()
    generate_tech_bar_stacked()
    generate_tech_bar_vs_hist()
    generate_tech_pie_basic()
    generate_tech_pie_examples()
    generate_tech_dashboard()
    
    # 演習
    generate_exercise_1_bar()
    generate_exercise_3_barh()
    generate_exercise_4_hist()
    generate_exercise_5_hist_bins()
    generate_exercise_6_pie()
    generate_exercise_7_pie_pct()
    generate_exercise_8_boxplot()
    generate_exercise_9_grouped()
    generate_exercise_10_stacked()
    
    # 応用問題
    generate_app_monthly_sales()
    generate_app_sales_breakdown()
    generate_app_score_analysis()
    generate_app_sales_dashboard()
    
    print("=" * 50)
    print("All images generated successfully!")
    print(f"Output directory: {output_dir}")

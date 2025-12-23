#!/usr/bin/env python3
"""
CH7-Section1 用の画像を生成するスクリプト
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # GUI不要のバックエンド

import os

# 画像保存先
output_dir = os.path.dirname(os.path.abspath(__file__)) + "/images"
os.makedirs(output_dir, exist_ok=True)

# =============================================================================
# 技術説明用の画像
# =============================================================================

# 1. plt.plot() の基本 (tech_plot_basic.png)
def generate_tech_plot_basic():
    x = [1, 2, 3, 4, 5]
    y = [10, 40, 20, 50, 30]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linewidth=2, markersize=8)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('plt.plot(x, y)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_plot_basic.png", dpi=150)
    plt.close()
    print("Generated: tech_plot_basic.png")

# 2. y データだけを渡す場合 (tech_plot_y_only.png)
def generate_tech_plot_y_only():
    y = [10, 40, 20, 50, 30]
    
    plt.figure(figsize=(8, 5))
    plt.plot(y, marker='o', linewidth=2, markersize=8)
    plt.xlabel('x (auto: 0, 1, 2, 3, 4)', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('plt.plot(y) - x is automatically 0, 1, 2, ...', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_plot_y_only.png", dpi=150)
    plt.close()
    print("Generated: tech_plot_y_only.png")

# 3. Figure と Axes を明示的に作成 (tech_fig_ax.png)
def generate_tech_fig_ax():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    x = [1, 2, 3, 4, 5]
    y = [10, 40, 20, 50, 30]
    ax.plot(x, y, marker='o', linewidth=2, markersize=8)
    
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('fig, ax = plt.subplots()', fontsize=14)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_fig_ax.png", dpi=150)
    plt.close()
    print("Generated: tech_fig_ax.png")

# 4. 複数の線を描く (tech_multiple_lines.png)
def generate_tech_multiple_lines():
    months = [1, 2, 3, 4, 5]
    sales_2023 = [100, 120, 150, 180, 200]
    sales_2024 = [120, 150, 200, 250, 300]
    
    plt.figure(figsize=(8, 5))
    plt.plot(months, sales_2023, marker='o', linewidth=2, markersize=8, label="2023")
    plt.plot(months, sales_2024, marker='s', linewidth=2, markersize=8, label="2024")
    
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Sales', fontsize=12)
    plt.title('Sales Comparison by Year', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_multiple_lines.png", dpi=150)
    plt.close()
    print("Generated: tech_multiple_lines.png")

# 5. 実践：簡単な売上グラフ (tech_sales_example.png)
def generate_tech_sales_example():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [100, 150, 120, 200, 250, 300]
    
    plt.figure(figsize=(10, 6))
    plt.plot(months, sales, marker='o', linewidth=2, markersize=8)
    
    plt.title("Monthly Sales 2024", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Sales (10,000 yen)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tech_sales_example.png", dpi=150)
    plt.close()
    print("Generated: tech_sales_example.png")

# =============================================================================
# 演習用の画像
# =============================================================================

# 6. 問題 1-1 期待する出力 (exercise_1_1.png)
def generate_exercise_1_1():
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 15, 35, 20]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linewidth=2, markersize=8)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_1_1.png", dpi=150)
    plt.close()
    print("Generated: exercise_1_1.png")

# 7. 問題 2-1 期待する出力 (exercise_2_1.png)
def generate_exercise_2_1():
    days = [1, 2, 3, 4, 5, 6, 7]
    temp = [20, 22, 19, 25, 28, 26, 23]
    
    plt.figure(figsize=(8, 5))
    plt.plot(days, temp, marker='o', linewidth=2, markersize=8)
    plt.title("Temperature", fontsize=14)
    plt.xlabel("Day", fontsize=12)
    plt.ylabel("Celsius", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_2_1.png", dpi=150)
    plt.close()
    print("Generated: exercise_2_1.png")

# 8. 問題 3-1 期待する出力 (exercise_3_1.png)
def generate_exercise_3_1():
    x = [1, 2, 3, 4, 5]
    y1 = [10, 20, 30, 40, 50]
    y2 = [15, 25, 20, 35, 45]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y1, marker='o', linewidth=2, markersize=8, label='y1')
    plt.plot(x, y2, marker='s', linewidth=2, markersize=8, label='y2')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/exercise_3_1.png", dpi=150)
    plt.close()
    print("Generated: exercise_3_1.png")

# =============================================================================
# 応用問題用の画像
# =============================================================================

# 9. 応用問題1: 週間気温グラフ - タスク1 (app_weekly_temp.png)
def generate_app_weekly_temp():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    high_temp = [25, 27, 24, 28, 30, 29, 26]
    low_temp = [18, 19, 17, 20, 22, 21, 19]
    
    plt.figure(figsize=(10, 6))
    plt.plot(days, high_temp, marker='o', linewidth=2, markersize=8, label="High")
    plt.plot(days, low_temp, marker='o', linewidth=2, markersize=8, label="Low")
    
    plt.title("Weekly Temperature", fontsize=16)
    plt.xlabel("Day", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_weekly_temp.png", dpi=150)
    plt.close()
    print("Generated: app_weekly_temp.png")

# 10. 応用問題2: 月別売上比較 - タスク2 (app_sales_comparison.png)
def generate_app_sales_comparison():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales_2022 = [100, 120, 90, 110, 130, 150, 160, 140, 120, 130, 150, 180]
    sales_2023 = [110, 130, 100, 120, 140, 160, 170, 150, 130, 140, 160, 190]
    sales_2024 = [120, 140, 110, 130, 150, 170, 180, 160, 140, 150, 170, 200]
    
    plt.figure(figsize=(14, 6))
    plt.plot(months, sales_2022, marker='o', linewidth=2, markersize=6, label="2022")
    plt.plot(months, sales_2023, marker='s', linewidth=2, markersize=6, label="2023")
    plt.plot(months, sales_2024, marker='^', linewidth=2, markersize=6, label="2024")
    
    plt.title("Monthly Sales Comparison", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_sales_comparison.png", dpi=150)
    plt.close()
    print("Generated: app_sales_comparison.png")

# 11. 応用問題4: 2つの y 軸 (app_dual_axis.png)
def generate_app_dual_axis():
    import pandas as pd
    
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": [100, 150, 120, 200, 250, 300],
        "Customers": [50, 75, 60, 100, 125, 150]
    })
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # 左の y 軸: Sales
    color1 = 'tab:blue'
    ax1.plot(df["Month"], df["Sales"], color=color1, marker='o', 
             linewidth=2, markersize=8, label="Sales")
    ax1.set_xlabel("Month", fontsize=12)
    ax1.set_ylabel("Sales", color=color1, fontsize=12)
    ax1.tick_params(axis='y', labelcolor=color1)
    
    # 右の y 軸: Customers
    ax2 = ax1.twinx()
    color2 = 'tab:red'
    ax2.plot(df["Month"], df["Customers"], color=color2, marker='s', 
             linewidth=2, markersize=8, label="Customers")
    ax2.set_ylabel("Customers", color=color2, fontsize=12)
    ax2.tick_params(axis='y', labelcolor=color2)
    
    plt.title("Sales and Customers", fontsize=16)
    
    # 凡例を結合
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=11)
    
    ax1.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_dual_axis.png", dpi=150)
    plt.close()
    print("Generated: app_dual_axis.png")

# =============================================================================
# すべての画像を生成
# =============================================================================

if __name__ == "__main__":
    print("Generating images for CH7-Section1...")
    print("=" * 50)
    
    # 技術説明
    generate_tech_plot_basic()
    generate_tech_plot_y_only()
    generate_tech_fig_ax()
    generate_tech_multiple_lines()
    generate_tech_sales_example()
    
    # 演習
    generate_exercise_1_1()
    generate_exercise_2_1()
    generate_exercise_3_1()
    
    # 応用問題
    generate_app_weekly_temp()
    generate_app_sales_comparison()
    generate_app_dual_axis()
    
    print("=" * 50)
    print("All images generated successfully!")
    print(f"Output directory: {output_dir}")

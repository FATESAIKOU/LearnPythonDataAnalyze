"""
CH7-Section4: グラフの装飾
画像生成スクリプト
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

def tech_presentation():
    """8. プレゼンテーション品質のグラフ"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales_2023 = [80, 95, 110, 105, 125, 130]
    sales_2024 = [90, 110, 120, 130, 150, 160]

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.plot(months, sales_2023, 'o-', 
            color='#3498db', linewidth=2.5, markersize=10, 
            label='2023', markeredgecolor='white', markeredgewidth=2)
    ax.plot(months, sales_2024, 's--', 
            color='#e74c3c', linewidth=2.5, markersize=10, 
            label='2024', markeredgecolor='white', markeredgewidth=2)

    ax.set_title('Monthly Sales Comparison\n2023 vs 2024', 
                 fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('Month', fontsize=14, labelpad=10)
    ax.set_ylabel('Sales (10,000 yen)', fontsize=14, labelpad=10)

    ax.set_ylim(70, 170)
    ax.grid(True, linestyle='--', alpha=0.5, axis='y')
    ax.legend(loc='upper left', fontsize=12, frameon=True, 
              facecolor='white', edgecolor='gray', shadow=True)
    ax.tick_params(axis='both', labelsize=12)

    ax.annotate('New Campaign\nStarted', 
                xy=(4, 150), xytext=(2.5, 155),
                fontsize=11, color='#e74c3c',
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))

    ax.set_facecolor('#fafafa')
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tech_presentation.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: tech_presentation.png")


# ============================================
# 演習用
# ============================================

def exercise_1_title():
    """演習1: タイトルの装飾"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-o')
    plt.title('Sales Report', fontsize=16, fontweight='bold', color='darkblue')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    
    plt.savefig(os.path.join(output_dir, 'exercise_1_title.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_1_title.png")


def exercise_2_labels():
    """演習2: 軸ラベルの装飾"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-o')
    plt.title('Sales Report', fontsize=16)
    plt.xlabel('Month', fontsize=14, color='gray')
    plt.ylabel('Sales', fontsize=14, color='gray')
    
    plt.savefig(os.path.join(output_dir, 'exercise_2_labels.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_2_labels.png")


def exercise_3_rotation():
    """演習3: x軸の目盛りを回転"""
    categories = ['January', 'February', 'March', 'April', 'May']
    values = [100, 120, 110, 130, 140]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, values)
    plt.xticks(rotation=45, ha='right')
    plt.title('Monthly Sales')
    plt.ylabel('Sales')
    plt.tight_layout()
    
    plt.savefig(os.path.join(output_dir, 'exercise_3_rotation.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_3_rotation.png")


def exercise_4_legend_pos():
    """演習4: 凡例の位置を変える"""
    x = [1, 2, 3, 4, 5]
    y1 = [10, 20, 15, 25, 20]
    y2 = [8, 18, 12, 22, 18]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, 'r-o', label='Product A')
    plt.plot(x, y2, 'b-s', label='Product B')
    plt.legend(loc='lower right')
    plt.title('Product Comparison')
    
    plt.savefig(os.path.join(output_dir, 'exercise_4_legend_pos.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_4_legend_pos.png")


def exercise_5_legend_detail():
    """演習5: 凡例の詳細設定"""
    x = [1, 2, 3, 4, 5]
    y1 = [10, 20, 15, 25, 20]
    y2 = [8, 18, 12, 22, 18]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, 'r-o', label='Product A')
    plt.plot(x, y2, 'b-s', label='Product B')
    plt.legend(
        title='Products',
        fontsize=12,
        frameon=True,
        shadow=True,
        facecolor='white'
    )
    plt.title('Product Comparison')
    
    plt.savefig(os.path.join(output_dir, 'exercise_5_legend_detail.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_5_legend_detail.png")


def exercise_6_grid():
    """演習6: グリッドの追加"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    plt.figure(figsize=(10, 6))
    plt.bar(x, y)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.title('Sales')
    
    plt.savefig(os.path.join(output_dir, 'exercise_6_grid.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_6_grid.png")


def exercise_7_ylim():
    """演習7: 軸の範囲を設定"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-o')
    plt.ylim(0, 50)
    plt.title('Sales Trend')
    
    plt.savefig(os.path.join(output_dir, 'exercise_7_ylim.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_7_ylim.png")


def exercise_8_text():
    """演習8: テキストを追加"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-o')
    plt.text(4, 35, 'Peak', fontsize=12, color='red', ha='center', va='bottom')
    plt.title('Sales Trend')
    plt.ylim(0, 45)
    
    plt.savefig(os.path.join(output_dir, 'exercise_8_text.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_8_text.png")


def exercise_9_annotate():
    """演習9: 矢印付き注釈"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-o')
    plt.annotate('Maximum Value',
                 xy=(4, 35),
                 xytext=(3, 45),
                 fontsize=12,
                 arrowprops=dict(arrowstyle='->', color='red', lw=2))
    plt.title('Sales Trend')
    plt.ylim(0, 50)
    
    plt.savefig(os.path.join(output_dir, 'exercise_9_annotate.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_9_annotate.png")


def exercise_10_save():
    """演習10: 高解像度で保存"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-o')
    plt.title('Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(True, alpha=0.3)
    
    plt.savefig(os.path.join(output_dir, 'exercise_10_save.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: exercise_10_save.png")


# ============================================
# 応用問題用
# ============================================

def app_business_report():
    """応用問題1: ビジネスレポート用グラフ"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [80, 95, 110, 125, 140, 155]
    target = [100, 100, 110, 120, 130, 140]

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.plot(months, sales, 'o-', color='#3498db', linewidth=2.5, 
            markersize=10, label='Sales', markeredgecolor='white', markeredgewidth=2)
    ax.plot(months, target, '--', color='#e74c3c', linewidth=2, label='Target')

    ax.set_title('Monthly Sales vs Target', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Month', fontsize=12, labelpad=10)
    ax.set_ylabel('Sales (10,000 yen)', fontsize=12, labelpad=10)
    ax.set_ylim(60, 170)
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)
    ax.legend(loc='lower right', fontsize=11, frameon=True, shadow=True, facecolor='white')
    ax.tick_params(axis='both', labelsize=11)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'app_business_report.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_business_report.png")


def app_annotations():
    """応用問題2: 複数の注釈"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
    sales = [80, 75, 90, 120, 135, 125, 140, 155]

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.plot(months, sales, 'o-', color='#2ecc71', linewidth=2.5, markersize=10)

    ax.annotate('New Product\nLaunch',
                xy=(2, 90),
                xytext=(0.5, 105),
                fontsize=11,
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=2),
                bbox=dict(boxstyle='round', facecolor='#e8f4f8', edgecolor='#3498db'))

    ax.annotate('Peak\nReached',
                xy=(4, 135),
                xytext=(5.5, 145),
                fontsize=11,
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2),
                bbox=dict(boxstyle='round', facecolor='#fdeaea', edgecolor='#e74c3c'))

    ax.text(7, 155 + 5, f'{sales[-1]}', fontsize=12, ha='center', fontweight='bold', color='#27ae60')

    ax.set_title('Monthly Sales Trend with Annotations', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Sales (10,000 yen)', fontsize=12)
    ax.set_ylim(60, 180)
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'app_annotations.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_annotations.png")


def app_custom_grid():
    """応用問題3: カスタム目盛りとグリッド"""
    x = list(range(0, 101, 10))
    y = [0, 5, 15, 30, 50, 65, 75, 82, 88, 93, 100]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, y, 'o-', color='#9b59b6', linewidth=2, markersize=8)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.minorticks_on()
    ax.grid(True, which='major', linestyle='-', linewidth=0.8, alpha=0.7)
    ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.4)

    ax.set_title('Progress Curve with Custom Grid', fontsize=14, fontweight='bold')
    ax.set_xlabel('Time (%)', fontsize=12)
    ax.set_ylabel('Completion (%)', fontsize=12)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'app_custom_grid.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_custom_grid.png")


def app_style_comparison():
    """応用問題4: スタイルの比較"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 20, 35, 30]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Default style
    axes[0].plot(x, y, 'o-', linewidth=2, markersize=8, color='#1f77b4')
    axes[0].set_title('Default Style', fontsize=14)
    axes[0].set_xlabel('X')
    axes[0].set_ylabel('Y')
    axes[0].grid(True, alpha=0.3)

    # ggplot style simulation
    axes[1].set_facecolor('#E5E5E5')
    axes[1].plot(x, y, 'o-', linewidth=2, markersize=8, color='#E24A33')
    axes[1].set_title('ggplot Style', fontsize=14)
    axes[1].set_xlabel('X')
    axes[1].set_ylabel('Y')
    axes[1].grid(True, color='white', linewidth=1.5)

    # Dark grid style simulation
    axes[2].set_facecolor('#EAEAF2')
    axes[2].plot(x, y, 'o-', linewidth=2, markersize=8, color='#4C72B0')
    axes[2].set_title('Seaborn Style', fontsize=14)
    axes[2].set_xlabel('X')
    axes[2].set_ylabel('Y')
    axes[2].grid(True, color='white', linewidth=1.5)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'app_style_comparison.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_style_comparison.png")


def app_dashboard():
    """応用問題5: プロフェッショナルなダッシュボード"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [100, 120, 115, 140, 160, 175]
    target = [110, 115, 120, 130, 145, 160]

    products = ['A', 'B', 'C', 'D']
    product_sales = [35, 28, 22, 15]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Upper: Line chart
    ax1.plot(months, sales, 'o-', color='#27ae60', linewidth=2.5, 
             markersize=10, label='Sales', markeredgecolor='white', markeredgewidth=2)
    ax1.plot(months, target, 's--', color='#e74c3c', linewidth=2, 
             markersize=8, label='Target')

    # Find first month where sales > target
    for i, (s, t) in enumerate(zip(sales, target)):
        if s > t:
            ax1.annotate('Target\nAchieved!',
                         xy=(i, s),
                         xytext=(i + 0.3, s + 10),
                         fontsize=9,
                         color='#27ae60',
                         fontweight='bold',
                         arrowprops=dict(arrowstyle='->', color='#27ae60', lw=1.5))
            break

    ax1.set_title('Monthly Sales vs Target', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Month', fontsize=11)
    ax1.set_ylabel('Sales (10,000 yen)', fontsize=11)
    ax1.set_ylim(80, 200)
    ax1.legend(loc='upper left', fontsize=10, frameon=True, facecolor='white')
    ax1.grid(True, axis='y', linestyle='--', alpha=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Lower: Horizontal bar chart
    colors = ['#3498db', '#2980b9', '#1f618d', '#154360']
    bars = ax2.barh(products, product_sales, color=colors, edgecolor='white', height=0.6)

    for bar, val in zip(bars, product_sales):
        ax2.text(val + 1, bar.get_y() + bar.get_height()/2, 
                 f'{val}%', va='center', fontsize=11, fontweight='bold')

    ax2.set_title('Sales by Product', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Share (%)', fontsize=11)
    ax2.set_xlim(0, 45)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.grid(True, axis='x', linestyle='--', alpha=0.5)

    fig.suptitle('Sales Dashboard - Q2 2024', fontsize=18, fontweight='bold', y=0.98)

    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    plt.savefig(os.path.join(output_dir, 'app_dashboard.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: app_dashboard.png")


# ============================================
# メイン
# ============================================

if __name__ == '__main__':
    print("Generating Section4 images...")
    
    # 技術説明
    tech_presentation()
    
    # 演習
    exercise_1_title()
    exercise_2_labels()
    exercise_3_rotation()
    exercise_4_legend_pos()
    exercise_5_legend_detail()
    exercise_6_grid()
    exercise_7_ylim()
    exercise_8_text()
    exercise_9_annotate()
    exercise_10_save()
    
    # 応用問題
    app_business_report()
    app_annotations()
    app_custom_grid()
    app_style_comparison()
    app_dashboard()
    
    print(f"\nAll images saved to: {output_dir}")

# Adventure Game 🎮

一個使用 Python 和 Pygame 開發的 2D 冒險遊戲，採用物件導向程式設計 (OOP) 架構

## 技術架構

本專案採用物件導向程式設計 (OOP) 架構，主要包含以下類別：

- **Game**: 主遊戲類別，負責遊戲循環、事件處理和畫面渲染
- **Spritesheet**: 精靈圖表處理類別
- **mixer**: 音效管理類別
- **Player**: 玩家角色類別
- **Enemy**: 敵人 AI 類別
- **Weapon**: 武器系統類別
- **Block/Water/Lava/Stone**: 各種地形物件類別

## 環境需求

- Python 3.7+
- Pygame 2.0+

## 安裝與設定

### 1. 建立虛擬環境

```bash
# 建立虛擬環境
python -m venv adventure_game_env

# 啟動虛擬環境
# Windows:
adventure_game_env\Scripts\activate
# macOS/Linux:
source adventure_game_env/bin/activate
```

### 2. 安裝依賴套件

```bash
# 安裝 Pygame
pip install pygame

# 或使用 requirements.txt
pip install -r requirements.txt
```

### 3. 執行遊戲

```bash
python main.py
```

## 遊戲操作

- **方向鍵 (↑↓←→)**: 移動角色
- **空白鍵**: 攻擊
- **ESC**: 退出遊戲

## 專案結構

```
Advanture Game/
├── main.py              # 主程式入口
├── configuration.py     # 遊戲配置設定
├── sprites.py          # 精靈物件類別
├── weapons.py          # 武器系統類別
├── requirements.txt    # 依賴套件清單
├── assets/            # 遊戲資源
│   ├── images/        # 圖片資源
│   └── sounds/        # 音效資源
└── README.md          # 專案說明文件
```

## 地圖物件代號

遊戲地圖使用字元代號來表示不同物件：

- `B`: 牆壁 (Block)
- `P`: 玩家 (Player)
- `E`: 敵人 (Enemy)
- `R`: 水域 (Water)
- `W`: 武器 (Weapon)
- `M`: 藥水 (Medicine)
- `F`: 花朵 (Flower)
- `L`: 岩漿 (Lava)
- `S`: 石頭 (Stone)
- `C`: 營火 (Campfire)

## 開發者

- 111113221 數資AI組 董佳和

## 授權

此專案為學術作業用途。

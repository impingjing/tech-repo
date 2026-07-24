import numpy as np
import random

# ==========================================
# 1. 环境与超参数设置
# ==========================================
N_STATES = 6          # 一维网格的状态数量 (0 到 5)
ACTIONS = [0, 1]      # 动作空间：0代表向左，1代表向右
GOAL_STATE = 5        # 状态 5 是终点（宝藏）

ALPHA = 0.1           # 学习率 (步长)
GAMMA = 0.9           # 折扣因子
EPSILON = 0.1         # epsilon-greedy 的探索率
EPISODES = 30         # 训练回合数

# ==========================================
# 2. 初始化 Q 表
# ==========================================
# 行代表状态 (0-5)，列代表动作 (0, 1)。初始 Q 值全部设为 0。
q_table = np.zeros((N_STATES, len(ACTIONS)))

# ==========================================
# 3. 策略定义：epsilon-greedy
# ==========================================
def choose_action(state, q_table):
    if random.uniform(0, 1) < EPSILON:
        # 探索：以 epsilon 的概率随机选择动作
        return random.choice(ACTIONS)
    else:
        # 利用：选择当前状态下 Q 值最大的动作
        # np.argmax 返回最大值对应的索引（即动作）
        return np.argmax(q_table[state, :])

# ==========================================
# 4. 环境交互逻辑 (Step 函数)
# ==========================================
def step(state, action):
    # 状态转移逻辑
    if action == 1:  # 向右走
        next_state = state + 1 if state < N_STATES - 1 else state
    else:            # 向左走
        next_state = state - 1 if state > 0 else state
    
    # 奖励函数与结束判断
    if next_state == GOAL_STATE:
        reward = 1.0  # 到达终点给奖励 1
        done = True   # 回合结束
    else:
        reward = 0.0  # 其他状态没有奖励
        done = False  # 回合继续
        
    return next_state, reward, done

# ==========================================
# 5. Sarsa 核心主循环
# ==========================================
for episode in range(EPISODES):
    state = 0  # 每一个 Episode 智能体都从最左侧起点 (状态 0) 开始
    
    # 【第一步】获取初始动作 A (基于初始状态 S)
    action = choose_action(state, q_table)
    done = False
    
    while not done:
        # 【第二步】执行动作 A，观察环境反馈的 R 和 S'
        next_state, reward, done = step(state, action)
        
        # 【第三步】同策略的关键：在 S' 下，再次使用当前策略选择 A'
        next_action = choose_action(next_state, q_table)
        
        # 【第四步】计算 Sarsa 更新目标并更新 Q 表
        q_predict = q_table[state, action]
        
        if not done:
            # 正常情况：TD Target = R + gamma * Q(S', A')
            q_target = reward + GAMMA * q_table[next_state, next_action]
        else:
            # 终点情况：由于游戏结束，没有未来的折扣价值了，Target 就是当前的即时奖励
            q_target = reward 
            
        # 套用更新公式：Q = Q + alpha * (Target - Predict)
        q_table[state, action] += ALPHA * (q_target - q_predict)
        
        # 【第五步】状态和动作转移，准备进入下一步循环
        state = next_state
        action = next_action

print("训练完成的 Q 表:")
print(np.round(q_table, 3))


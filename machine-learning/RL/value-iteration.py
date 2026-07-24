# 构建MDP

import numpy as np

# 1.定义基础参数
n_states = 3    # 状态空间 S：{0,1,2}
n_actions = 2   # 动作空间 A：{0,1}
gamma = 0.9     # 折扣因子
theta = 1e-4    # 收敛阈值（当价值变化极小时停止迭代）

# 2.定义转移概率和奖励函数（P和R）
# P[state][action]=[(probability,next_state,reward,is_done)]
P = {
    0:{
        0:[(1.0,0,0.0,False)], # 在状态0向左，撞墙，留在原地，加惩罚
        1:[(1.0,1,0.0,False)]  # 在状态0向右，到达状态1，无奖励
    },
    1:{
        0:[(1.0,0,0.0,False)], # 在状态1向左，到达状态0，无奖励
        1:[(1.0,2,1.0,True)]  # 在状态1向右，到达状态2，有奖励，游戏结束
    },
    2:{
        0:[(1.0,2,0.0,True)], # 终点状态，怎么走都留在原地
        1:[(1.0,2,0.0,True)]
    }
}

# 价值迭代算法实现
def value_iteration(n_states, n_actions, P, gamma, theta):
    # 初始化所有状态的价值为0
    V = np.zeros(n_states)

    iteration = 0
    while True:
        delta = 0 # 记录这一轮迭代中最大的价值变化量

        # 遍历每个状态 s
        for state in range(n_states):
            # 存储当前状态s下，左右可能动作的Q值
            Q_values = np.zeros(n_actions)
            # 遍历每个动作 a
            for action in range(n_actions):
                # 遍历所有可能的下个状态
                for prob,next_state,reward,done in P[state][action]:
                    # 计算动作价值 Q(s,a)
                    if done:
                        # 如果到达终点，没有未来的折扣奖励
                        Q_values[action] += prob*reward
                    else:
                        # 贝尔曼最优公式的内部求和部分
                        Q_values[action] += prob*(reward + gamma*V[next_state])

            # 找到当前状态的最优价值，并计算变化量
            best_value = np.max(Q_values)
            delta = max(delta, np.abs(best_value-V[state]))

            # 更新状态价值 V(s)
            V[state] = best_value

        iteration += 1
        # 如果所有状态的价值 变化量都小于阈值，说明已经收敛
        if delta < theta:
            print(f"Iteration {iteration}: Found optimal policy")
            break

    return V

# 运行算法
optimal_V = value_iteration(n_states, n_actions, P, gamma, theta)
print("optimal V: ", optimal_V)

# 策略提取
def extract_policy(V, n_states, n_actions, P, gamma):
    # 初始化最优策略
    optimal_policy = np.zeros(n_states,dtype=int)
    for state in range(n_states):
        Q_values = np.zeros(n_actions)
        for action in range(n_actions):
            for prob,next_state,reward,done in P[state][action]:
                if done:
                    Q_values[action] += prob*reward
                else:
                    Q_values[action] += prob*(reward + gamma*V[next_state])
        # 选择能带来最大 Q 值的动作
        optimal_policy[state] = np.argmax(Q_values)

    return optimal_policy

# 提取并打印策略
policy = extract_policy(optimal_V, n_states, n_actions, P, gamma)
print("optimal policy (0=leftwards,1=rightwards): ", policy)


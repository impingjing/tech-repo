import numpy as np

# --- 1. 定义环境 (与价值迭代相同) ---
n_states = 3
n_actions = 2
gamma = 0.9
theta = 1e-4

P = {
    0: {0: [(1.0, 0, 0.0, False)], 1: [(1.0, 1, 0.0, False)]},
    1: {0: [(1.0, 0, 0.0, False)], 1: [(1.0, 2, 1.0, True)]},
    2: {0: [(1.0, 2, 0.0, True)], 1: [(1.0, 2, 0.0, True)]}
}


# --- 2. 策略评估 (Policy Evaluation) ---
def policy_evaluation(policy, P, n_states, gamma, theta):
    """
    计算给定策略下每个状态的价值 (使用贝尔曼期望方程)
    """
    V = np.zeros(n_states)  # 初始化状态价值

    while True:
        delta = 0
        # 遍历每一个状态
        for s in range(n_states):
            v_old = V[s]
            new_v = 0

            # 在策略评估中，我们按照当前策略 policy 规定的动作去走
            a = policy[s]

            # 遍历该动作可能导致的所有转移
            for prob, next_s, reward, done in P[s][a]:
                if done:
                    new_v += prob * reward
                else:
                    new_v += prob * (reward + gamma * V[next_s])

            V[s] = new_v
            delta = max(delta, np.abs(v_old - V[s]))

        # 当所有状态价值的变化量都小于阈值时，评估收敛
        if delta < theta:
            break

    return V


# --- 3. 策略改进 (Policy Improvement) ---
def policy_improvement(V, P, n_states, n_actions, gamma):
    """
    根据当前评估出的价值函数，贪心地生成新策略
    """
    policy = np.zeros(n_states, dtype=int)

    for s in range(n_states):
        Q_values = np.zeros(n_actions)
        # 计算当前状态下，所有动作的 Q 值
        for a in range(n_actions):
            for prob, next_s, reward, done in P[s][a]:
                if done:
                    Q_values[a] += prob * reward
                else:
                    Q_values[a] += prob * (reward + gamma * V[next_s])

        # 贪心选择：将 Q 值最大的动作设为该状态的新策略
        policy[s] = np.argmax(Q_values)

    return policy


# --- 4. 策略迭代主循环 (Policy Iteration) ---
def policy_iteration(P, n_states, n_actions, gamma, theta):
    # 1. 随机初始化一个策略 (这里初始化为全0动作，即全向左走)
    policy = np.zeros(n_states, dtype=int)

    iteration = 0
    while True:
        iteration += 1

        # 步骤 A: 策略评估 (算出当前策略到底有多好)
        V = policy_evaluation(policy, P, n_states, gamma, theta)

        # 步骤 B: 策略改进 (基于算出的价值，寻找更好的策略)
        new_policy = policy_improvement(V, P, n_states, n_actions, gamma)

        # 检查策略是否发生变化
        # 如果新策略和老策略完全一样，说明已经达到最优，停止迭代
        if np.array_equal(new_policy, policy):
            print(f"策略迭代在第 {iteration} 轮收敛。")
            break

        # 否则，更新策略，继续下一轮
        policy = new_policy

    return policy, V


# --- 5. 运行算法 ---
optimal_policy, optimal_V = policy_iteration(P, n_states, n_actions, gamma, theta)

print("最优状态价值 (V*):", optimal_V)
print("最优策略 (0=左, 1=右):", optimal_policy)
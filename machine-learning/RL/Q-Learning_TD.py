import random

import numpy as np


# ==========================================
# 1. 环境与超参数设置
# ==========================================
# 这里使用一个最小化的一维网格世界来演示 Q-Learning。
#
# 状态空间：0 -> 1 -> 2 -> 3 -> 4 -> 5
# 起点：状态 0
# 终点：状态 5
#
# 每一步智能体只能选择两个动作：
# 0: 向左移动
# 1: 向右移动
#
# 这个环境足够简单，适合用来理解 Q-Learning 的核心思想。

N_STATES = 6
ACTIONS = [0, 1]
GOAL_STATE = 5

ALPHA = 0.1
GAMMA = 0.9
EPSILON = 0.1
EPISODES = 30
MAX_STEPS_PER_EPISODE = 100


# ==========================================
# 2. 初始化 Q 表
# ==========================================
# Q 表的形状是：[状态数, 动作数]
# q_table[s, a] 表示：在状态 s 下执行动作 a 的长期价值估计。
# 初始时全部设为 0，表示“还没有经验”。
q_table = np.zeros((N_STATES, len(ACTIONS)))


# ==========================================
# 3. epsilon-greedy 策略
# ==========================================
def choose_action(state, q_table):
	"""根据 epsilon-greedy 策略选择动作。

	1. 以 EPSILON 的概率随机探索，避免智能体过早只盯着当前最优动作。
	2. 其余情况选择当前 Q 值最大的动作，利用已有经验。

	当多个动作的 Q 值相同的时候，随机从并列最优动作中选一个，
	这样可以避免初始阶段总是偏向动作 0。
	"""

	if random.uniform(0, 1) < EPSILON:
		return random.choice(ACTIONS)

	state_action_values = q_table[state]
	max_value = np.max(state_action_values)
	best_actions = np.where(state_action_values == max_value)[0]
	return int(np.random.choice(best_actions))


# ==========================================
# 4. 环境交互逻辑
# ==========================================
def step(state, action):
	"""执行一次动作，返回环境反馈。

	返回值：
	next_state: 动作执行后的新状态
	reward:     即时奖励
	done:       当前回合是否结束

	环境规则非常简单：
	- 向右移动：状态编号 +1
	- 向左移动：状态编号 -1
	- 如果撞到边界，就停留在边界状态，不会越界
	- 到达终点状态 5 时，得到奖励 1，并结束回合
	"""

	if action == 1:
		next_state = state + 1 if state < N_STATES - 1 else state
	else:
		next_state = state - 1 if state > 0 else state

	if next_state == GOAL_STATE:
		reward = 1.0
		done = True
	else:
		reward = 0.0
		done = False

	return next_state, reward, done


# ==========================================
# 5. Q-Learning 更新公式
# ==========================================
def q_learning_update(q_table, state, action, reward, next_state, done):
	"""执行一次 Q-Learning 更新。

	Q-Learning 属于 off-policy 算法，核心更新目标为：

		target = reward + gamma * max_a Q(next_state, a)

	如果当前已经到达终点，则没有后续状态价值，目标就是当前奖励：

		target = reward

	最后用增量式更新把当前估计向目标靠近：

		Q(s, a) <- Q(s, a) + alpha * (target - Q(s, a))
	"""

	current_q = q_table[state, action]

	if done:
		target_q = reward
	else:
		target_q = reward + GAMMA * np.max(q_table[next_state])

	q_table[state, action] += ALPHA * (target_q - current_q)


# ==========================================
# 6. 训练主循环
# ==========================================
def train_q_learning():
	"""训练 Q-Learning 智能体，并返回训练后的 Q 表。"""

	for episode in range(EPISODES):
		# 每个回合都从起点开始。
		state = 0
		done = False
		steps = 0

		# 一个回合最多执行 MAX_STEPS_PER_EPISODE 步，防止极端情况下死循环。
		while not done and steps < MAX_STEPS_PER_EPISODE:
			# 先根据当前状态选择动作。
			action = choose_action(state, q_table)

			# 与环境交互，得到下一状态、奖励和结束标志。
			next_state, reward, done = step(state, action)

			# 按照 Q-Learning 的公式更新 Q 表。
			q_learning_update(q_table, state, action, reward, next_state, done)

			# 状态向前推进，进入下一轮交互。
			state = next_state
			steps += 1

		if done:
			print(f"Episode {episode + 1:02d}: finished in {steps} steps")
		else:
			print(f"Episode {episode + 1:02d}: reached step limit ({MAX_STEPS_PER_EPISODE})")

	return q_table


# ==========================================
# 7. 运行训练并打印结果
# ==========================================
if __name__ == "__main__":
	trained_q_table = train_q_learning()

	print("\n训练完成后的 Q 表:")
	print(np.round(trained_q_table, 3))

	# 每个状态下 Q 值最大的动作，就是当前学到的“贪心策略”。
	best_actions = np.argmax(trained_q_table, axis=1)
	print("\n每个状态对应的最优动作(0=left, 1=right):")
	print(best_actions)

# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # 创建图数据
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# # 创建轨迹数据
# trajectories = [[1, 2, 3, 4, 1], [3, 2, 4, 1, 3]]

# # 创建图形对象
# fig, ax = plt.subplots()

# # 初始化绘图
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True)

# lines = []
# for trajectory in trajectories:
#     line, = ax.plot([], [], linewidth=2, marker='o')
#     lines.append(line)

# # 更新函数，用于更新轨迹位置
# def update(i):
#     for j, trajectory in enumerate(trajectories):
#         current_node = trajectory[i]
#         x = pos[current_node][0]
#         y = pos[current_node][1]
#         lines[j].set_data(x, y)
#     return lines

# # 创建动画
# ani = FuncAnimation(fig, update, frames=len(trajectories[0]), interval=2, blit=True)

# plt.show()


print("hello world!")
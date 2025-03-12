import gym
import numpy as np

env = gym.make('CartPole-v0')
obs = env.reset()

print("env loaded successfully")
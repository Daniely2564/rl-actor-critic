import gym
from agent import Agent
from blackjack import BlackjackEnv

# env = BlackjackEnv()
env = gym.make('Blackjack-v0')
agent = Agent()

obs = env.reset()

print(obs)
obs_, reward, done, info = env.step(1)
print(obs_, reward, done, info)
obs_, reward, done, info = env.step(0)
print(obs_, reward, done, info)
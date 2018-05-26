from setuptools import setup

setup(
    name='gym_exploration_chain',
    version='0.0.2',
    description='OpenAI Gym interface to deep exploration chain problem described in Bootstrapped DQN',
    author='Intel AI Lab Haifa',
    author_email='itai.caspi@intel.com',
    license='Apache',
    packages=['gym_exploration_chain'],
    install_requires=["gym==0.9.4", "numpy"],
)

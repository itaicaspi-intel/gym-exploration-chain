import os

from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup

abs_path = os.path.dirname(os.path.abspath(__file__))
requirements_file = os.path.join(abs_path, 'requirements.txt')
install_requirements = parse_requirements(requirements_file, session=PipSession())
requirements = [str(ir.req) for ir in install_requirements]

setup(
    name='gym_exploration_chain',
    version='0.0.1',
    description='OpenAI Gym interface to deep exploration chain problem described in Bootstrapped DQN',
    author='Intel AI Lab Haifa',
    author_email='itai.caspi@intel.com',
    license='Apache',
    packages=['gym_exploration_chain'],
    install_requires=requirements,
)

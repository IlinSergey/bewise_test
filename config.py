from environs import Env


env = Env()
env.read_env()


DB = env('DB')

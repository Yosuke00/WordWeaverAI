from colorama import Fore, Style
from enum import Enum

class AgentColor(Enum):
    '''
    各エージェントの出力結果を色で区別するためのクラス
    '''
    ChiefDirector = Fore.LIGHTBLACK_EX
    ItViewer = Fore.LIGHTRED_EX
    Proofreader = Fore.LIGHTGREEN_EX
    ItResearcher = Fore.LIGHTBLUE_EX
    TestReader = Fore.LIGHTYELLOW_EX
    
def print_agent_output(output:str, agent:str ="ChiefDirector"):
    '''
    Agentの出力に色をつける関数
    '''
    print(f"{AgentColor[agent].value}{agent}: {output}{Style.RESET_ALL}")
import random


class Solution:
    """
    sentence: noun_phrase verb_phrase
    noun_phrase: Article Adj* noun
    Adj*: null|Adj Adj*
    verb_phrase: verb noun_phrase

    Article => 一个|这个
    noun=> 女人|篮球|桌子|小猫
    verb=> 看着|听着|看见
    Adj=> 蓝色的|好看的|小小的|年轻的
    """

    def __init__(self):
        self.patten = {'sentence': ('noun_phrase', 'verb_phrase'),
                       'noun_phrase': ('Article', 'Adj*', 'noun'),
                       'Adj*': (None, 'Adj'),
                       'verb_phrase': ('verb', 'noun_phrase')}
        self.vocab = {'Article': ('一个', '这个'),
                      'noun': ('女人', '篮球', '桌子', '小猫'),
                      'verb': ('看着', '听着', '看见'),
                      'Adj': ('蓝色的', '好看的', '小小的', '年轻的')}

    def _generator(self, target: str, rst: 'List[str]') -> str:
        if target in self.patten:
            if target == 'Adj*':
                chosen = set()
                adj = random.choice(self.patten[target])
                while adj:
                    adj_word = random.choice(self.vocab[adj])
                    if adj_word in chosen:
                        break
                    chosen.add(adj_word)
                    rst.append(adj_word)
                    adj = random.choice(self.patten[target])
            else:
                for _ in self.patten[target]:
                    self._generator(_, rst)
        else:
            rst.append(random.choice(self.vocab[target]))
        return rst

    def generator(self, target: str):
        if target not in self.patten:
            return None
        rst = []
        return ''.join(self._generator(target, rst))


if __name__ == '__main__':
    Generator = Solution()
    print(Generator.generator('sentence'))
    print(Generator.generator('sentence'))
    print(Generator.generator('sentence'))
    print(Generator.generator('noun_phrase'))
    print(Generator.generator('Adj*'))
    print(Generator.generator('verb_phrase'))
    print("---------------------------------")
    print(Generator.generator('other_patten'))

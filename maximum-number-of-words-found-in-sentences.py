class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max_sentence_length = 0
        
        current_sentence_length = 0
        
        for i in range(0, len(sentences)):
            sentence = sentences[i].split()
            current_sentence_length = len(sentence)
            if max_sentence_length < current_sentence_length:
                max_sentence_length = current_sentence_length
                current_sentence_length = 0
            else:
                current_sentence_length = 0
        return max_sentence_length
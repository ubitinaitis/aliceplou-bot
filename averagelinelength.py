lyrics = open("C:/Users/bitin/OneDrive/Desktop/bot/lyrics.txt", "r", encoding='utf-8')

def averageLineLength():
        lyrics = open("C:/Users/bitin/OneDrive/Desktop/bot/lyrics.txt", "r", encoding='utf-8')
        lines = lyrics.readlines()
        return sum([len(line.strip('\n')) for line in lines]) / len(lines)

print(averageLineLength())
#!/usr/bin/env python3
import sys

# Função do Mapper
def mapper():
    for line in sys.stdin:
        line = line.strip()
        fields = line.split(",")
        
        if len(fields) == 4:
            id = fields[0]
            # Pseudonimização simples
            pseudonym = "user_" + id
            anonymized_data = f"{id},{pseudonym},***,***"
            print(anonymized_data)

if __name__ == "__main__":
    mapper()

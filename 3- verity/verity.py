import sys

def solve():
    # Read all input from standard input (stdin)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    # Read number of test cases
    try:
        T = int(next(iterator))
    except StopIteration:
        return
    
    for _ in range(T):
        N = int(next(iterator))
        K = int(next(iterator))
        
        # Read the K available characters
        chars = [next(iterator) for _ in range(K)]
        
        # Track confirmed characters for each index (None if unknown)
        result = [None] * N
        
        # Iterate through available characters to discover each position
        # We only need to query up to K - 1 characters, as any remaining unknown positions
        # must be the last remaining character.
        for char_idx in range(K - 1):
            target_char = chars[char_idx]
            
            # Formulate guess: keep already discovered characters in their places,
            # and place target_char in all currently unrevealed positions.
            guess = []
            for i in range(N):
                if result[i] is not None:
                    guess.append(result[i])
                else:
                    guess.append(target_char)
            
            guess_str = "".join(guess)
            print(guess_str)
            
            # Read feedback from the judge / input file
            response = next(iterator)
            
            # If the guess happened to be entirely correct early, move to next test case
            if response == "CORRECT":
                break
            
            # Update known positions based on feedback
            for i in range(N):
                if response[i] != '_':
                    result[i] = response[i]
        else:
            # For any remaining unknown positions, fill them with the last character
            last_char = chars[-1]
            for i in range(N):
                if result[i] is None:
                    result[i] = last_char
            
            # Final output for the test case
            final_guess = "".join(result)
            print(final_guess)
            
            # Read response for the final guess (if available in input)
            try:
                response = next(iterator)
            except StopIteration:
                pass

if __name__ == "__main__":
    solve()
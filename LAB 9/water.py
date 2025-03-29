import time
import math
import random

class WaterJugsGame:
    def __init__(self, capacity_a, capacity_b, target):
        self.capacity_a = capacity_a
        self.capacity_b = capacity_b
        self.target = target
        self.current_state = (0, 0)  # Initial state: both jugs empty
    
    def is_goal_state(self, state):
        """Check if the target volume is reached in either jug."""
        return state[0] == self.target or state[1] == self.target
    
    def is_valid_state(self, state):
        """Check if a state is valid (within jug capacities)."""
        x, y = state
        return 0 <= x <= self.capacity_a and 0 <= y <= self.capacity_b
    
    def get_valid_moves(self, state):
        """Generate all valid moves from the current state."""
        x, y = state
        moves = []
        
        # Fill either jug completely
        if x < self.capacity_a:
            moves.append((self.capacity_a, y))  # Fill jug A
        if y < self.capacity_b:
            moves.append((x, self.capacity_b))  # Fill jug B
        
        # Empty either jug completely
        if x > 0:
            moves.append((0, y))  # Empty jug A
        if y > 0:
            moves.append((x, 0))  # Empty jug B
        
        # Pour water from one jug to the other
        if x > 0 and y < self.capacity_b:
            pour_amount = min(x, self.capacity_b - y)
            moves.append((x - pour_amount, y + pour_amount))  # Pour from A to B
        
        if y > 0 and x < self.capacity_a:
            pour_amount = min(y, self.capacity_a - x)
            moves.append((x + pour_amount, y - pour_amount))  # Pour from B to A
        
        # Remove duplicates and the current state
        valid_moves = [move for move in moves if move != state]
        return valid_moves
    
    def utility(self, state, maximizing_player):
        """Evaluate the utility of a state."""
        if self.is_goal_state(state):
            return 100 if maximizing_player else -100
        
        # Calculate how close each jug is to the target
        distance_a = abs(state[0] - self.target)
        distance_b = abs(state[1] - self.target)
        min_distance = min(distance_a, distance_b)
        
        # The closer to the target, the better
        score = (self.capacity_a + self.capacity_b - min_distance) / (self.capacity_a + self.capacity_b)
        
        return score if maximizing_player else -score
    
    def minimax(self, state, depth, maximizing_player):
        """Standard Minimax algorithm implementation."""
        if depth == 0 or self.is_goal_state(state):
            return self.utility(state, maximizing_player), None
        
        valid_moves = self.get_valid_moves(state)
        if not valid_moves:  # No valid moves left, it's a draw
            return 0, None
        
        best_move = None
        
        if maximizing_player:
            max_eval = float('-inf')
            for move in valid_moves:
                eval_score, _ = self.minimax(move, depth - 1, False)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in valid_moves:
                eval_score, _ = self.minimax(move, depth - 1, True)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
            return min_eval, best_move
    
    def alpha_beta(self, state, depth, alpha, beta, maximizing_player):
        """Minimax with Alpha-Beta pruning for improved efficiency."""
        if depth == 0 or self.is_goal_state(state):
            return self.utility(state, maximizing_player), None
        
        valid_moves = self.get_valid_moves(state)
        if not valid_moves:  # No valid moves left, it's a draw
            return 0, None
        
        best_move = None
        
        if maximizing_player:
            max_eval = float('-inf')
            for move in valid_moves:
                eval_score, _ = self.alpha_beta(move, depth - 1, alpha, beta, False)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in valid_moves:
                eval_score, _ = self.alpha_beta(move, depth - 1, alpha, beta, True)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval, best_move
    
    def get_ai_move(self, state, use_alpha_beta=True, depth=5):
        """Get the best move for the AI using either Minimax or Alpha-Beta pruning."""
        if use_alpha_beta:
            _, best_move = self.alpha_beta(state, depth, float('-inf'), float('inf'), True)
        else:
            _, best_move = self.minimax(state, depth, True)
        return best_move
    
    def is_solvable(self):
        """Check if the problem is solvable using Bézout's identity."""
        gcd = math.gcd(self.capacity_a, self.capacity_b)
        return self.target % gcd == 0 and self.target <= max(self.capacity_a, self.capacity_b)
    
    def display_state(self, state):
        """Display the current state of the jugs."""
        print(f"Jug A ({self.capacity_a}L): {state[0]}L")
        print(f"Jug B ({self.capacity_b}L): {state[1]}L")
        print(f"Target: {self.target}L")
        print("-" * 30)
    
    def play_game(self, use_alpha_beta=True):
        """Play the game with a human player against the AI."""
        print("\nWater Jugs Game")
        print(f"Jug A capacity: {self.capacity_a}L")
        print(f"Jug B capacity: {self.capacity_b}L")
        print(f"Target: {self.target}L")
        
        if not self.is_solvable():
            print("Warning: This configuration may not be solvable!")
        
        current_player = "Human"  # Human goes first
        self.current_state = (0, 0)  # Start with empty jugs
        
        while True:
            print(f"\n{current_player}'s turn")
            self.display_state(self.current_state)
            
            if self.is_goal_state(self.current_state):
                print(f"{current_player} wins!")
                break
            
            valid_moves = self.get_valid_moves(self.current_state)
            if not valid_moves:
                print("No valid moves left. It's a draw!")
                break
            
            if current_player == "Human":
                print("Available moves:")
                for i, move in enumerate(valid_moves, 1):
                    print(f"{i}. Jug A: {move[0]}L, Jug B: {move[1]}L")
                
                while True:
                    try:
                        choice = int(input("Enter your move number: ")) - 1
                        if 0 <= choice < len(valid_moves):
                            self.current_state = valid_moves[choice]
                            break
                        else:
                            print("Invalid choice. Try again.")
                    except ValueError:
                        print("Please enter a number.")
                
                current_player = "AI"
            else:  # AI's turn
                print("AI is thinking...")
                
                # Time the AI's decision-making
                start_time = time.time()
                ai_move = self.get_ai_move(self.current_state, use_alpha_beta)
                end_time = time.time()
                
                print(f"AI chose: Jug A: {ai_move[0]}L, Jug B: {ai_move[1]}L")
                print(f"Decision time: {end_time - start_time:.6f} seconds")
                
                self.current_state = ai_move
                current_player = "Human"

def compare_algorithms(game, state, depth=5, iterations=10):
    """Compare the performance of Minimax and Alpha-Beta pruning."""
    print("\nPerformance Comparison:")
    
    # Minimax timing
    minimax_times = []
    for _ in range(iterations):
        start_time = time.time()
        game.minimax(state, depth, True)
        end_time = time.time()
        minimax_times.append(end_time - start_time)
    
    avg_minimax_time = sum(minimax_times) / iterations
    
    # Alpha-Beta timing
    alpha_beta_times = []
    for _ in range(iterations):
        start_time = time.time()
        game.alpha_beta(state, depth, float('-inf'), float('inf'), True)
        end_time = time.time()
        alpha_beta_times.append(end_time - start_time)
    
    avg_alpha_beta_time = sum(alpha_beta_times) / iterations
    
    print(f"Average Minimax time: {avg_minimax_time:.7f} seconds")
    print(f"Average Alpha-Beta time: {avg_alpha_beta_time:.7f} seconds")
    print(f"Improvement: {(avg_minimax_time - avg_alpha_beta_time) / avg_minimax_time * 100:.2f}%")

def main():
    # Default game parameters
    capacity_a = 5
    capacity_b = 3
    target = 4
    
    # Allow custom parameters
    print("Water Jugs Game Setup")
    print("(Press Enter to use default values)")
    
    try:
        input_a = input(f"Enter capacity of jug A (default {capacity_a}): ")
        if input_a:
            capacity_a = int(input_a)
        
        input_b = input(f"Enter capacity of jug B (default {capacity_b}): ")
        if input_b:
            capacity_b = int(input_b)
        
        input_target = input(f"Enter target volume (default {target}): ")
        if input_target:
            target = int(input_target)
    except ValueError:
        print("Invalid input. Using default values.")
    
    game = WaterJugsGame(capacity_a, capacity_b, target)
    
    # Compare algorithm performance
    compare_algorithms(game, (0, 0))
    
    # Play the game
    use_alpha_beta = input("Use Alpha-Beta pruning? (y/n, default: y): ").lower() != 'n'
    game.play_game(use_alpha_beta)

if __name__ == "__main__":
    main()
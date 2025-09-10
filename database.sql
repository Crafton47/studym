-- Create the leaderboard table
CREATE TABLE IF NOT EXISTS leaderboard (
    rank INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    score INTEGER NOT NULL
);

-- Insert sample data
INSERT OR REPLACE INTO leaderboard (rank, name, score) VALUES (1, 'Alex Johnson', 95);
INSERT OR REPLACE INTO leaderboard (rank, name, score) VALUES (2, 'Sarah Chen', 92);
INSERT OR REPLACE INTO leaderboard (rank, name, score) VALUES (3, 'Mike Davis', 88);
INSERT OR REPLACE INTO leaderboard (rank, name, score) VALUES (4, 'Emma Wilson', 85);
INSERT OR REPLACE INTO leaderboard (rank, name, score) VALUES (5, 'John Smith', 82);
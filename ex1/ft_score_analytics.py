#!/usr/bin/env python3
import sys


def main() -> None:
    """PixelMetrics 3000's leaderboard"""

    print("=== Player Score Analytics ===")
    ac = len(sys.argv)
    if ac == 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
            )
        return
    try:
        # 1.リスト化して保存
        scores: list[int] = []
        for v in sys.argv[1:]:
            scores += [int(v)]

        # 2.Scores表示
        print(f"Scores processed: {scores}")

        # 3.Players表示
        print(f"Total players: {len(scores)}")

        # 4.Total_score表示
        print(f"Total score: {sum(scores)}")

        # 5.Average表示
        print(f"Average score: {sum(scores) / len(scores)}")

        # 6.High_score表示
        print(f"High score: {max(scores)}")

        # 7.Low_score表示
        print(f"Low score: {min(scores)}")

        # 8.Score_range表示
        print(f"Score range: {max(scores) - min(scores)}")
    except Exception as e: # noqa
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

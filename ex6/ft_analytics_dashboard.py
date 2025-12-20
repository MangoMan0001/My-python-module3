#!/usr/bin/env python3


def main() -> None:
    """list,dict,set DEMO"""

    data = {
        'players': {
            'alice': {
                'level': 41,
                'total_score': 2824,
                'sessions_played': 13,
                'favorite_mode': 'ranked',
                'achievements_count': 5
            },
            'bob': {
                'level': 16,
                'total_score': 4657,
                'sessions_played': 27,
                'favorite_mode': 'ranked',
                'achievements_count': 2
            },
            'charlie': {
                'level': 44,
                'total_score': 9935,
                'sessions_played': 21,
                'favorite_mode': 'ranked',
                'achievements_count': 7
            },
            'diana': {
                'level': 3,
                'total_score': 1488,
                'sessions_played': 21,
                'favorite_mode': 'casual',
                'achievements_count': 4
            },
            'eve': {
                'level': 33,
                'total_score': 1434,
                'sessions_played': 81,
                'favorite_mode': 'casual',
                'achievements_count': 7
            },
            'frank': {
                'level': 15,
                'total_score': 8359,
                'sessions_played': 85,
                'favorite_mode': 'competitive',
                'achievements_count': 1
            }
        },
        'sessions': [
            {
                'player': 'bob',
                'duration_minutes': 94,
                'score': 1831,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'bob',
                'duration_minutes': 32,
                'score': 1478,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'diana',
                'duration_minutes': 17,
                'score': 1570,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 98,
                'score': 1981,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'diana',
                'duration_minutes': 15,
                'score': 2361,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'eve',
                'duration_minutes': 29,
                'score': 2985,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 34,
                'score': 1285,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'alice',
                'duration_minutes': 53,
                'score': 1238,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 1555,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'frank',
                'duration_minutes': 92,
                'score': 2754,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 98,
                'score': 1102,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'diana',
                'duration_minutes': 39,
                'score': 2721,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 46,
                'score': 329,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'charlie',
                'duration_minutes': 56,
                'score': 1196,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 117,
                'score': 1388,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'diana',
                'duration_minutes': 118,
                'score': 2733,
                'mode': 'competitive',
                'completed': True
            },
            {
                'player': 'charlie',
                'duration_minutes': 22,
                'score': 1110,
                'mode': 'ranked',
                'completed': False
            },
            {
                'player': 'frank',
                'duration_minutes': 79,
                'score': 1854,
                'mode': 'ranked',
                'completed': False
            },
            {
                'player': 'charlie',
                'duration_minutes': 33,
                'score': 666,
                'mode': 'ranked',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 101,
                'score': 292,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 25,
                'score': 2887,
                'mode': 'competitive',
                'completed': True
            },
            {
                'player': 'diana',
                'duration_minutes': 53,
                'score': 2540,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'eve',
                'duration_minutes': 115,
                'score': 147,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 118,
                'score': 2299,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 42,
                'score': 1880,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 97,
                'score': 1178,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 18,
                'score': 2661,
                'mode': 'competitive',
                'completed': True
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 761,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 46,
                'score': 2101,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'charlie',
                'duration_minutes': 117,
                'score': 1359,
                'mode': 'casual',
                'completed': True
            }
        ],
        'game_modes': [
            'casual',
            'competitive',
            'ranked'
        ],
        'achievements': [
            'first_blood',
            'level_master',
            'speed_runner',
            'treasure_seeker',
            'boss_hunter',
            'pixel_perfect',
            'combo_king',
            'explorer'
        ]
    }

    # 1.=== Game Analytics Dashboard ===
    print("=== Game Analytics Dashboard ===")
    print()

    # 2.=== List Comprehension Examples ===
    print("=== List Comprehension Examples ===")
    top_players = [name for name, stats in data['players'].items()
                   if 2000 < stats['total_score']]
    print(f"High scorers (>2000): {top_players}")
    ranker = [name for name, stats in data['players'].items()
              if stats['favorite_mode'] == "ranked"]
    print(f"ranker : {ranker}")
    high_level_players = [name for name, stats in data["players"].items()
                          if 30 < stats["level"]]
    print(f"high level players = {high_level_players}")
    print()

    # 3.=== Dict Comprehension Examples ===
    print("=== Dict Comprehension Examples ===")
    scores = {name: stats["total_score"]
              for name, stats in data["players"].items()}
    print(f"Player scores: {scores}")
    status_list = [s['completed'] for s in data['sessions']]
    sessions = {str(status): status_list.count(status)
                for status in [True, False]}
    print(f"Succes sessions: {sessions}")
    achievement_count = {name: count['achievements_count']
                         for name, count in data['players'].items()}
    print(f"Achievement counts: {achievement_count}")
    print()

    # 4.=== Set Comprehension Examples ===
    print("=== Set Comprehension Examples ===")
    sesiion_players = {s['player'] for s in data['sessions']}
    print(f"Session Players: {sesiion_players}")
    sesiion_mode = {s['mode'] for s in data['sessions']}
    print(f"Session mode: {sesiion_mode}")
    player_level = {s['level'] for s in data['players'].values()}
    print(f"Player level: {player_level}")
    print()

    # 5.=== Combined Analysis ===
    total_score = sum(s['total_score'] for s in data['players'].values())
    total_player = len(data['players'])
    top_player = max([(s['total_score'], name)
                      for name, s in data['players'].items()])
    print("=== Combined Analysis ===")
    print(f"Total players: {total_player}\n"
          f"Total unique achievements: {len(data['achievements'])}\n"
          "Average score: "
          f" {total_score / total_player:.1f}\n"
          f"Top performer: {top_player[1]} ({top_player[0]} points, "
          f"{data['players'][top_player[1]]['achievements_count']} "
          "achievements)"
          )


if __name__ == "__main__":
    main()

from typing import Dict, Any
import random


def analyze_video(video_path: str) -> Dict[str, Any]:
    """
    FAKE analysis function.
    Later you replace this with real AI / CV models.
    Right now it just returns example data in the structure
    you might want for your scouting report.
    """

    players = [
        {
            "number": 3,
            "name": "Guard #3",
            "estimated_points": 18,
            "fg_attempts": 12,
            "threes_attempted": 7,
            "usage_rate": 0.28,
            "tendencies": [
                "Pull-up threes from the left wing",
                "Strong right-hand drives",
                "Likes high pick-and-roll as ball handler",
            ],
        },
        {
            "number": 12,
            "name": "Wing #12",
            "estimated_points": 14,
            "fg_attempts": 10,
            "threes_attempted": 4,
            "usage_rate": 0.22,
            "tendencies": [
                "Catches and shoots from corners",
                "Backdoor cuts when overplayed",
            ],
        },
        {
            "number": 15,
            "name": "Big #15",
            "estimated_points": 10,
            "fg_attempts": 8,
            "threes_attempted": 0,
            "usage_rate": 0.18,
            "tendencies": [
                "Rolls hard out of ball screens",
                "Crashes offensive glass",
            ],
        },
    ]

    random.shuffle(players)

    team_summary = {
        "estimated_possessions": 65 + random.randint(-5, 5),
        "pace_comment": "Medium pace, similar to a typical high school game.",
        "offensive_style": [
            "Heavy high pick-and-roll with #3 as primary handler",
            "Spot-up shooters in both corners",
        ],
        "defensive_style": [
            "Mostly man-to-man",
            "Occasional 2-3 zone after timeouts",
            "Some full-court token pressure after made baskets",
        ],
    }

    plays = [
        {
            "name": "High PnR",
            "frequency_estimate": "40% of half-court possessions",
            "description": "Guard #3 uses high screen from #15 at the top; #15 rolls hard, #12 spots up weak-side.",
        },
        {
            "name": "Horns set",
            "frequency_estimate": "15% of half-court possessions",
            "description": "Both bigs at elbows; guard chooses a side ball screen, weak-side shooter lifts to the slot.",
        },
        {
            "name": "Baseline out-of-bounds (BLOB – box)",
            "frequency_estimate": "Used on most baseline inbounds",
            "description": "Box alignment into screen-the-screener action for corner three.",
        },
    ]

    defense = {
        "base_defense": "Man-to-man",
        "zone_usage": "2-3 zone roughly 20% of the time, usually after timeouts or in 4th quarter.",
        "pressure": "Soft full-court man pressure after makes; mostly to slow you down, not to trap.",
        "key_defenders": [
            "#3 pressures the ball full court.",
            "#15 protects the rim but can be late on closeouts.",
        ],
    }

    return {
        "video_path": video_path,
        "team_summary": team_summary,
        "players": players,
        "plays": plays,
        "defense": defense,
        "notes_for_coach": [
            "Make #3 work on defense – attack him in switches to tire him out.",
            "Force #3 left and go under on screens unless he’s hot from three.",
            "Attack #15 in space – use 5-out or pick-and-pop to pull him away from the rim.",
        ],
    }

# AlchemyRiddle Progression Probe 0.1.0

Read-only research probe for Graveyard Keeper 1.407.

Purpose:
- confirm the alchemy Technology backbone in loaded GameBalance;
- census explicit UnlockAlchemy / UnlockRandomAlchemy disclosure channels in loaded FlowCanvas graphs and item on-use expressions;
- capture bounded structural neighborhoods around the early Clotho / Merchant alchemy paths;
- never log exact mixed-alchemy formula IDs or ingredient rows.

Expected log markers:
- AR_PROGRESSION_BEGIN
- AR_PROGRESSION_TECH
- AR_PROGRESSION_DISCLOSURE
- AR_PROGRESSION_FOCUS_BEGIN / NODE / EDGE / DONE
- AR_PROGRESSION_SUMMARY
- AR_PROGRESSION_DONE

Safety:
- no save mutation;
- no balance mutation;
- no inventory mutation;
- no craft unlock mutation;
- no UI injection;
- one read-only census after game start.

# 📝 Router Setup Summary: Oburec_Father

## 🚀 Overview
Successfully reconfigured the router (192.168.3.1) for DPI bypass using **Zapret** after the removal of `zapret2`. The setup is optimized for YouTube (video + previews) and is designed to run alongside **ZeroBlock**.

## 🛠️ Components
- **Zapret (Routerich)**: Installed via `opkg` package (v72.20251122).
- **Nfqws**: Handles DPI bypass on queue 200.
- **Firewall (fw4)**: Integration via `/etc/nftables.d/10-zapret.nft`.

## ⚙️ Key Settings
- **Zapret Mark**: `0x2` (set via `DESYNC_MARK=0x2`).
- **ZeroBlock Mark**: `0x40000000` (ignored by Zapret rules to avoid loops).
- **IPv6**: Disabled in Zapret for stability.
- **TCP Strategy**: `fake,split2` with `autottl` and `md5sig` fooling.
- **UDP Strategy**: `fake` (6 repeats) for QUIC.

## 📂 File Locations
- **Router Config**: `/opt/zapret/config`
- **Router NFT Rules**: `/etc/nftables.d/10-zapret.nft`
- **AGrav Backup**: `c:\Oburec\Antigravity\Projects\AGrav\temp\Oburec_Father\`

## 🔄 Restoration Steps
1. Perform cleanup (see `CLEANUP_INSTRUCTIONS.md`).
2. Install Zapret via LuCI or `opkg install zapret`.
3. Copy `zapret_config.txt` to `/opt/zapret/config`.
4. Copy `10-zapret.nft` to `/etc/nftables.d/10-zapret.nft`.
5. Restart service: `/etc/init.d/zapret restart`.
6. Reload firewall: `fw4 reload`.

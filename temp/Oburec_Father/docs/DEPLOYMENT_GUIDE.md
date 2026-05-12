# 📖 Router DPI Bypass Deployment Guide

This guide describes how to replicate the **Oburec_Father** setup on any OpenWrt router.

## 📁 Repository Structure
- `configs/zapret_config.txt`: The optimized Zapret configuration.
- `firewall/10-zapret.nft`: Nftables rules for redirection and loop prevention.
- `scripts/ssh_manager.py`: Python script for remote management via SSH (requires `paramiko`).
- `docs/SUMMARY.md`: Overview of the original setup.

## 🛠️ Step-by-Step Installation

### 1. Preparation
- Ensure the router has internet access.
- Ensure SSH is enabled (default port 22).
- Identify the router architecture (`uname -m`).

### 2. Install Zapret
- Download the latest release from `https://github.com/bol-van/zapret/releases`.
- Extract it to `/opt/zapret`.
- Run `./install_bin.sh` to link binaries for the detected architecture.

### 3. Deploy Configuration
- Upload `configs/zapret_config.txt` to the router at `/opt/zapret/config`.
- (Optional) If using ZeroBlock, ensure `DESYNC_MARK` in the config is set to `0x2` and doesn't conflict with other services.

### 4. Configure Firewall
- Upload `firewall/10-zapret.nft` to the router at `/etc/nftables.d/10-zapret.nft`.
- **CRITICAL**: If the LAN interface name is not `br-lan`, update the `iifname` in the `.nft` file accordingly.
- Reload firewall: `fw4 reload`.

### 5. Start Service
- Symlink the init script: `ln -sf /opt/zapret/init.d/sysv/zapret /etc/init.d/zapret`.
- Enable and start:
  ```bash
  /etc/init.d/zapret enable
  /etc/init.d/zapret restart
  ```

## 🔍 Troubleshooting
- **Check Traffic**: Run `nft list chain inet fw4 zapret_custom_forward` to see if packet counters are increasing.
- **Check Processes**: Run `ps | grep nfqws` to ensure the daemon is running.
- **Conflict with VPN**: If using a VPN (like WARP/Wireguard), ensure the marks are correctly handled to avoid infinite loops.
- **IPv6 Issues**: If thumbnails/video fail on mobile, ensure `DISABLE_IPV6=1` in the config (unless you've fully tuned IPv6).
- **Opkg Install Error (Status 44)**: If `opkg install zapret` fails with "preinst script returned status 44", it means there are conflicting manual files. Run this cleanup before installing:
  ```bash
  /etc/init.d/zapret stop
  rm -rf /opt/zapret /etc/init.d/zapret /etc/rc.d/S*zapret* /etc/nftables.d/10-zapret.nft
  ```

## 🚀 Automation
You can use `scripts/ssh_manager.py` to automate these steps. Example:
```bash
python scripts/ssh_manager.py write configs/zapret_config.txt /opt/zapret/config
python scripts/ssh_manager.py cmd "/etc/init.d/zapret restart"
```

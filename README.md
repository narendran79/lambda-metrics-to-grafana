# lambda-metrics-to-grafana 🚀

Monitor AWS Lambda success and error metrics in Grafana — serverless style.

## 🔧 What It Does
- Emits custom CloudWatch metrics from two Lambda functions (Success & Error).
- A third Lambda collects these metrics every 30 mins via EventBridge.
- Metrics are visualized in Grafana using CloudWatch as a data source.

## ⚙️ Setup
1. Deploy 3 Lambda functions:
   - `sucessMetrics.py`
   - `errorMetrics.py`
   - `metricsCollector.py`
2. Create EventBridge Scheduler (cron: every 30 mins).
3. Use EC2 instance for Grafana. I will include my Installation Commands below.
3. Add CloudWatch as a data source in Grafana.
4. Build dashboard panels for `SuccessCount` and `ErrorCount`.

## 🛠️ Tech Stack
- AWS Lambda
- Amazon CloudWatch
- EventBridge Scheduler
- Grafana

## 🔧 Installation of Grafana in EC2
1  sudo apt update
2  sudo apt-get install -y apt-transport-https software-properties-common
3  sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
4  wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
5  sudo apt-get update
6  sudo apt-get install grafana
7  sudo systemctl enable grafana-server
8  sudo systemctl start grafana-server

After Installation you can access the grafana through 3000 port
`https:\\<ec2-public-ip>:3000`

## Additional Setup
- If you want to add alert through Grafana, we can create alert_id to send the email if its exceeds the given limit


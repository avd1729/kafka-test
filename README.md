# Steps to Run Zookeeper, Kafka, and Create a Topic

## Step 1: Start Zookeeper
1. Open **Command Prompt** or **PowerShell**.
2. Navigate to Kafka's `bin\windows` directory:
   ```powershell
   cd C:\kafka\bin\windows
3. Run the following command to start Zookeeper:
   ```powershell
   .\zookeeper-server-start.bat ..\..\config\zookeeper.properties

## Step 2: Start Kafka
1. Open a new **Command Prompt** or **PowerShell** window.
2. Navigate to Kafka's bin\windows directory:
    ```powershell
   cd C:\kafka\bin\windows
3. Run the following command to start Kafka:
   ```powershell
   .\kafka-server-start.bat ..\..\config\server.properties

## Step 3: Creating a topic
1. Open another **Command Prompt** or **PowerShell** window.
2. Navigate to Kafka's `bin\windows` directory:
   ```powershell
   cd C:\kafka\bin\windows
3. Run the following command to create a topic named test-topic:
   ```powershell
   .\kafka-topics.bat --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
4. Verify the topic creation:
   ```powershell
   .\kafka-topics.bat --list --bootstrap-server localhost:9092







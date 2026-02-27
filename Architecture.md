#  System Architecture

## Overview
The Notification Prioritization Engine processes incoming events and decides whether to Send Now, Later, or Never.

## Core Components

### 1. Event Ingestion Service
Receives notification events from multiple services.

### 2. Decision Engine
Applies priority scoring and classification logic.

### 3. Deduplication Module
Prevents exact and near-duplicate notifications.

### 4. Rules Engine
Allows configurable rules without redeployment.

### 5. Scheduler
Stores deferred notifications for later delivery.

### 6. Dispatcher
Sends notifications via push, email, SMS, or in-app.

### 7. Audit Logger
Logs decisions with explanation for transparency.

## Flow

Event → Decision Engine  
↓  
Deduplication & Rules  
↓  
(NOW | LATER | NEVER)  
↓  
Scheduler / Dispatcher  
↓  
User  
↓  
Audit Logs

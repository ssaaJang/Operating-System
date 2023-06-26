# Process_Id : 프로세스 번호
# arrival_time : 도착 시간
# burst_time : CPU 버스트 시간
# time_slice : 일정시간마다 프로세스 강제 교체 (Time Quantum)

import matplotlib.pyplot as plt

class Process:
    def __init__(self,Process_Id,arrival_time,burst_time):
        self.Process_Id = Process_Id
        self.arrival_time = arrival_time
        self.burst_time = burst_time

class RoundRobin:
    def __init__(self,time_slice):
        self.time_slice = time_slice
        self.ready_queue = []
    
    def add_process(self, process):
        self.ready_queue.append(process)
    
    def schedule(self):
        current_time = 0
        Trace_Time = []
        while self.ready_queue:
            process = self.ready_queue.pop(0)
            if process.burst_time > self.time_slice:
                Trace_Time.append((process.Process_Id,current_time,current_time+self.time_slice))
                print(f"Running process {process.Process_Id} for time slice {self.time_slice}.")
                current_time += self.time_slice               
                process.burst_time -= self.time_slice
                self.ready_queue.append(process)
            else:
                Trace_Time.append((process.Process_Id,current_time,current_time+process.burst_time))
                print(f"Running process {process.Process_Id} for remaining burst time {process.burst_time}.")
                current_time += process.burst_time
                process.burst_time = 0
                print(f"Process {process.Process_Id} completed at time {current_time}.")
        
        
       
        
        for pid, start, end in Trace_Time:
            plt.barh(y=pid,left=start,width=end-start,height=0.5)
        plt.xlabel("Time")
        plt.ylabel("Process ID")
        plt.title("Gantt")
        plt.yticks(range(1,len(Trace_Time)+1))
        plt.grid(True)
        plt.show()

        
scheduler = RoundRobin(time_slice=3)

process1 = Process(Process_Id=1, arrival_time=0, burst_time=8)
process2 = Process(Process_Id=2, arrival_time=3, burst_time=5)
process3 = Process(Process_Id=3, arrival_time=5, burst_time=10)

scheduler.add_process(process1)
scheduler.add_process(process2)
scheduler.add_process(process3)

scheduler.schedule()


import sun.util.calendar.LocalGregorianCalendar;

public class Task {

    private String name;
    private double duration;
    private int priority; //should only be 1-3 or 1-5, figure out the exception handling later.
    // Maybe priority should be more abstract, like "low, medium, high", something like that.

    // add dueDate later, it screws with the constructor right now.

    public Task(String name, double duration, int priority) {
        this.name = name;
        this.duration = duration;
        this.priority = priority;

    }


    public Task(String name, double duration) {
        this.name = name;
        this.duration = duration;
        this.priority = 0;
    }

    public Task(String name) {
        this.name = name;
        this.duration = 0;
        this.priority = 0;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getDuration() {
        return duration;
    }

    public void setDuration(double duration) {
        this.duration = duration;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    @Override
    public String toString(){
        return "Task{name: " + name + ", duration: " + duration + ", priority: " + priority + "}";
    }
}

import java.util.ArrayList;

public class Category {

    private String name;
    private ArrayList<Task> taskArrayList;

    public Category(String name){
        this.name = name;
        taskArrayList = new ArrayList<Task>();
    }

    public void addTask(String name, double duration, int priority){
        taskArrayList.add(new Task(name, duration, priority));
    }
    public void addTask(String name, double duration){
        taskArrayList.add(new Task(name, duration));
    }
    public void addTask(String name, int priority){
        taskArrayList.add(new Task(name, priority));
    }
    public void addTask(String name){
        taskArrayList.add(new Task(name));
    }

    public String getName() {
        return name;
    }

    public void listTasks(){
        for (int i=0; i<taskArrayList.size(); i++){
            System.out.println(taskArrayList.get(i).toString());
        }
    }

}

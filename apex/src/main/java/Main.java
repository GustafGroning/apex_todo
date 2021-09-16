public class Main {

    public static void main(String[] args) {


        Category category = new Category("work");
        category.addTask("plugga", 6.2, 3);
        category.listTasks();
    }
}

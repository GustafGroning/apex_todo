import java.util.ArrayList;

public class App {

    /*
    top level control, includes all the categories and has all methods related to top level stuff,
     such as "find a specific category", addCategory, etc.
     */

    private ArrayList<Category> categories;

    public App(){
        this.categories = new ArrayList<Category>();
    }

    public void addCategory(String name){
        this.categories.add(new Category(name));
    }

    public void listCategories(){
        for (int i=0; i<categories.size(); i++){
            System.out.println(categories.get(i).getName());
        }
    }
}

package Backend;

import lombok.Getter;
import lombok.Setter;

import java.util.Objects;

public class Space {

    @Getter
    private final String name;
    @Getter
    private final int location;

    /**
     * Constructor
     *
     * @param location The postion on the gameboard
     * @param name Name of the space
     */
    public Space(String name, int location) {
        this.name = name;
        this.location = location;
    }

    /**
     * Checks if Space is an instance of Property
     * @param space position on the game board
     * @return returns true if space is an instance of property
     */
    public boolean isProperty(Property space){
        return false;
    }

    @Override
    public String toString() {
        return "Space{" +
                "name='" + name + '\'' +
                ", location=" + location +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Space)) return false;
        Space space = (Space) o;
        return getLocation() == space.getLocation() && Objects.equals(getName(), space.getName());
    }
}

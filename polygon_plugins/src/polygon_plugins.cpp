#include <polygon_base/regular_polygon.hpp>
#include <cmath>

namespace polygon_plugins
{
    // The implementation of the Square and Triangle classes is fairly straightforward: save the side length, and use it to calculate the area. 
    class Square : public polygon_base::RegularPolygon
    {
        public:
        void initialize(double side_length) override
        {
            side_length_ = side_length;
        }

        double area() override
        {
            return side_length_ * side_length_;
        }

        protected:
        double side_length_;
    };

    class Triangle : public polygon_base::RegularPolygon
    {
        public:
        void initialize(double side_length) override
        {
            side_length_ = side_length;
        }

        double area() override
        {
            return 0.5 * side_length_ * getHeight();
        }

        double getHeight()
        {
            return sqrt((side_length_ * side_length_) - ((side_length_ / 2) * (side_length_ / 2)));
        }

        protected:
        double side_length_;
    };
}

// The only piece that is pluginlib specific is the last three lines, which invokes some magical macros that register the classes as actual plugins.
#include <pluginlib/class_list_macros.hpp>

// The fully-qualified type of the plugin class, in this case, polygon_plugins::Square
// The fully-qualified type of the base class, in this case, polygon_base::RegularPolygon
PLUGINLIB_EXPORT_CLASS(polygon_plugins::Square, polygon_base::RegularPolygon)
PLUGINLIB_EXPORT_CLASS(polygon_plugins::Triangle, polygon_base::RegularPolygon)